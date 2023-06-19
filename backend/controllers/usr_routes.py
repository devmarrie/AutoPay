# This script handles Google OAuth authentication using Flask Blueprint 
import os
import pathlib
from dotenv import load_dotenv

# flask libraries
import requests
from flask import Flask, session, abort, redirect, request, Blueprint
from flask_login import current_user, login_user, logout_user

# Google OAuth libraries
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

# Import models
from models.user import User
from models.database import db

load_dotenv()

# Load environment variables
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

# define blueprint
users_routes = Blueprint('users_routes', __name__)



os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" # to allow Http traffic for local dev


# Define Google client ID, secrets file, and flow object for authentication
GOOGLE_CLIENT_ID = GOOGLE_CLIENT_ID
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/login/callback"
)


# """Custom Authentication decorator function"""
# def login_is_required(function):
#     def wrapper(*args, **kwargs):
#         if "google_id" not in session:
#             return abort(401)  # Authorization required
#         else:
#             return function(*args, **kwargs)

#     return wrapper
@users_routes.route("/sign-in")
def signin():
    return redirect("get_needs", user=current_user)

# Initiate Google Auth
@users_routes.route("/login")
def login():
    """ Check user login """
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

# Google OAuth2 callback function to login user
@users_routes.route("/login/callback", methods=['GET', 'POST'])
def callback():
    """ Initiate Google OAuth2 flow """
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    
    # # Print user details
    # print("User ID:", id_info['sub'])
    # print("Email:", id_info['email'])
    # print("Name:", id_info['name'])
    # print("Profile Picture URL:", id_info['picture'])
    
    # return "Successfully authenticated!"

    # Check if user with same google id already exists
    user = User.query.filter_by(google_id=id_info.get("sub")).first()
    
    # Log in user if user exists
    if user:
        login_user(user)
        return "Already signed in"

    # Create a new User if google_id is not in database
    new_user = User(
        google_id=id_info.get("sub"),
        name=id_info.get("name"),
        email=id_info.get("email"),
        avatar_url=id_info.get("picture")
    )
    db.session.add(new_user)
    db.session.commit()

    # Log in new user
    login_user(new_user)
    return "Successfully athenticated"


# Route to log out user
@users_routes.route("/logout")
def logout():
    logout_user()
    return redirect('/')

