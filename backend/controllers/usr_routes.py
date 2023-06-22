from models.user import User
from models.database import db
from flask_bcrypt import Bcrypt
from flask import Flask, session, redirect, request, Blueprint,jsonify


users_routes = Blueprint('users_routes', __name__)

# bcrypt = Bcrypt()

# @users_routes.route("/sign-in", methods=['POST'])
# def signin():
#     username = request.json["username"]
#     password = request.json["password"]
#     phone_no = request.json["phone_no"]

#     user_exists = User.query.filter_by(username=username).first() is not None

#     if user_exists:
#         return jsonify({
#             "error": "User Already exists"
#         }), 409
#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#     new_user = User(username=username,password=hashed_password, phone_no=phone_no)
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({
#         "id": new_user.id,
#         "username": new_user.username
#     })

# @users_routes.route("/login", methods=['POST'])
# def login():
#     username = request.json["username"]
#     password = request.json["password"]

#     user = User.query.filter_by(username=username).first()

#     if user is None:
#         return jsonify({
#             "error": "User not found in db"
#         }), 401
#     if not bcrypt.check_password_hash(user.password.encode('utf-8'), password):
#         return jsonify({
#             "error": "Passwords do not match"
#         }), 401
    
#     session["user_id"] = user.id
#     print(session)

#     return jsonify({
#         "id": user.id,
#         "username": user.username
#     })

# @users_routes.route("/details", methods=['GET'])
# def view_details():
#     user_id = session.get("user_id")
#     if not user_id:
#         return jsonify({
#             "error": "Unathorized"
#         }), 401
    
#     user = User.query.filter_by(id=user_id).first()
#     if user is None:
#         return jsonify({
#             "error": "User not found"
#         }), 404

#     return jsonify({
#         "id": user.id,
#         "username": user.username
#     })

# # This script handles Google OAuth authentication using Flask Blueprint 
# import os
# import pathlib
# from dotenv import load_dotenv

# # flask libraries
# import requests
# from flask import Flask, session, abort, redirect, request, Blueprint,jsonify
# from flask_login import current_user, login_user, logout_user
# from flask_cors import cross_origin

# # Google OAuth libraries
# from google.oauth2 import id_token
# from google_auth_oauthlib.flow import Flow
# from pip._vendor import cachecontrol
# import google.auth.transport.requests

# # Import models
# from models.user import User
# from models.database import db

# load_dotenv()

# # Load environment variables
# GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
# GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

# # define blueprint
# users_routes = Blueprint('users_routes', __name__)



# os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" # to allow Http traffic for local dev


# # Define Google client ID, secrets file, and flow object for authentication
# GOOGLE_CLIENT_ID = GOOGLE_CLIENT_ID
# client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

# flow = Flow.from_client_secrets_file(
#     client_secrets_file=client_secrets_file,
#     scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
#     redirect_uri="http://127.0.0.1:5000/login/callback"
# )

# @users_routes.route("/sign-in")
# def signin():
#     return redirect("http://127.0.0.1:3000/needs")

# # Initiate Google Auth
# @users_routes.route("/api/register")
# @cross_origin(origins='http://127.0.0.1:3000', supports_credentials=True)
# def login():
#     """ Check user login """
#     authorization_url, state = flow.authorization_url()
#     session["state"] = state
#     return redirect(authorization_url)

# @users_routes.route('/login', methods=['POST'])
# def register_user():
#     try:
#         access_token = request.json.get('accessToken')
#         client_id = GOOGLE_CLIENT_ID  # Replace with your Google Client ID

#         # Verify the Google access token
#         id_info = id_token.verify_oauth2_token(access_token, requests.Request(), client_id)

#         # Extract user information from the verified token
#         user_id = id_info['sub']
#         email = id_info['email']
#         name = id_info['name']
#         print(user_id,email,name)
#         # Additional user data can be retrieved as needed

#         # Perform user registration logic here (e.g., create a new user record in the database)

#         # Return a success response to the frontend
#         return {'message': 'User registered successfully'}, 200
#     except Exception as e:
#         # Handle any errors that occur during registration
#         return {'message': 'User registration failed'}, 500


# # Google OAuth2 callback function to login user
# @users_routes.route("/login/callback", methods=['GET', 'POST'])
# def callback():
#     """ Initiate Google OAuth2 flow """
#     try:
#         flow.fetch_token(authorization_response=request.url)

#         if "state" not in session or session["state"] != request.args.get("state"):
#             return jsonify({"error": "Invalid state"}), 400

#         credentials = flow.credentials
#         request_session = requests.session()
#         cached_session = cachecontrol.CacheControl(request_session)
#         token_request = google.auth.transport.requests.Request(session=cached_session)

#         id_info = id_token.verify_oauth2_token(
#             id_token=credentials._id_token,
#             request=token_request,
#             audience=GOOGLE_CLIENT_ID
#         )

#         # Check if user with same google id already exists
#         user = User.query.filter_by(google_id=id_info.get("sub")).first()

#         # Log in user if user exists
#         if user:
#             login_user(user)
#             return redirect("http://127.0.0.1:3000/needs")

#         # Create a new User if google_id is not in the database
#         new_user = User(
#             google_id=id_info.get("sub"),
#             name=id_info.get("name"),
#             email=id_info.get("email"),
#             avatar_url=id_info.get("picture")
#         )
#         db.session.add(new_user)
#         db.session.commit()

#         # Log in new user
#         login_user(new_user)
#         return redirect("http://127.0.0.1:3000/needs")

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# # Route to log out user
# @users_routes.route("/logout")
# def logout():
#     logout_user()
#     return redirect('/')

