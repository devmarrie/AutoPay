from flask import Blueprint, jsonify, request, redirect, url_for, abort
from models.user import User
from models.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from flask_user import current_user, login_required
from flask import session
from dotenv import load_dotenv


# Google OAuth libraries
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
import google.auth.transport.requests
from pip._vendor import cachecontrol
import requests
import os
import pathlib

users_routes = Blueprint('user_routes', __name__)

load_dotenv()
# Load environment variables
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" #http traffic for local dev

# Google OAuth flow
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/login/callback"
)


"""Users routes"""
@users_routes.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return jsonify({"message": "User Authenticated"})
        # return redirect(url_for('dashboard'))
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        unhashed = data['password']
        phone_no = data['phone_no']

        password = generate_password_hash(unhashed)
        usr = User(username=username, phone_no=phone_no, password=password)
        db.session.add(usr)
        db.session.commit()
        #return redirect(url_for('login'))
        return jsonify({'message': 'User registered succesfully'})
        

@users_routes.route('/login')
def login():
    """ Check user login """
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)
    # if current_user.is_authenticated:
    #     return jsonify({"message": "User Authenticated"})
    # if request.method == 'POST':
    #     data = request.get_json()
    #     username = data['username']
    #     password = data['password']
    
    #     user = User.query.filter_by(username=username).first()
    #     if user and check_password_hash(user.password, password):
    #        login_user(user, remember=True)
    #        return  redirect(url_for('need_routes.add_need'))
    #        #return redirect('http://localhost:3000/needs')
    #     #    session_cookie_name = session_manager.session_cookie_name
    #     #    session_id = request.cookies.get(session_cookie_name)
    #     #    response = jsonify({'message': 'User logged in successfully'})
    #     #    response.set_cookie(current_app.config['SESSION_COOKIE_NAME'], session_id)
    #     else:
    #         return redirect(url_for('register'))
    #     #jsonify({'error': 'Invalid credentials'}), 401
    #     # session_cookie = request.headers.cookies.get('id')
@users_routes.route('/login/callback')
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

    # Check if user with same google id already exists
    # user = User.query.filter_by(google_id=id_info.get("sub")).first()
    
    # Log in user if user exists
    # if user:
    #     login_user(user)
    #     return (redirect('/get_needs'))
    
    # Print user details
    print("User ID:", id_info['sub'])
    print("Email:", id_info['email'])
    print("Name:", id_info['name'])
    print("Profile Picture URL:", id_info['picture'])
    
    return "Successfully authenticated!"

    # Create a new User if google_id is not in database
    # new_user = User(
    #     google_id=id_info.get("sub"),
    #     name=id_info.get("name"),
    #     email=id_info.get("email"),
    #     avatar_url=id_info.get("picture")
    # )
    # db.session.add(new_user)
    # db.session.commit()

    # # Log in new user
    # login_user(new_user)
    # return redirect('/get_needs')


@users_routes.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'User logged out successfully'})

@users_routes.route('/view_profile') 
def view_profile():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.filter_by(id=user_id).first()
        return jsonify(f'{user_id}: {user}')
    
    # user = current_user
    # return jsonify({
    #     'username': user.username,
    #     'phone_no': user.phone_no
    # })


# def get_users():
#     users =  User.query.all()
#     return jsonify([user.to_dict() for user in users])


@users_routes.route('/update_user', methods=['PUT'])
def update_user():
    user = current_user
    username = request.form['username']
    phone_no = request.form['phone_no']
    password = request.form['password']

    if username:
        user.username = username
    if phone_no:
        user.phone_no = phone_no
    if password:
        user.password = password
    db.session.commit()
    return jsonify(user.to_dict())    

@users_routes.route('/delete_user/<string:id>', methods=['DELETE'])
def del_need(id):
    u = User.query.get(id)
    if u:
        db.session. delete(u)
        db.session.commit()
        return jsonify({'message': f'User belonging to {id} deleted successfully'})
    else:
        return jsonify({'error': f'User with {id} not found'}), 404