from flask import Flask,session,redirect, request
from models.database import db, init_db
from flask_migrate import Migrate
from flask_user import UserManager
from flask_login import LoginManager, current_user, login_required
from dotenv import load_dotenv
from models.user import User
from flask_cors import CORS
from flask_session import Session
from controllers import need_routes, users_routes, pay_routes, hist_routes
import os

#google auth
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')


app = Flask(__name__)
app.secret_key = GOOGLE_CLIENT_SECRET
CORS(app, origins=['http://localhost:3000'], 
     methods=['GET', 'POST', 'PUT', 'DELETE'], 
     headers=['Content-Type', 'Authorization'], supports_credentials=True)

load_dotenv()
# Db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')
app.config['USER_EMAIL_SENDER_EMAIL'] = os.getenv('EMAIL')
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SESSION_TYPE'] = 'filesystem'


"""Mpesa Intergration"""
app.config["API_ENVIRONMENT"] = "sandbox" #sandbox or production
app.config["APP_KEY"] = os.getenv('CONSUMER_KEY')# App_key from developers portal
app.config["APP_SECRET"] = os.getenv('CONSUMER_SECRET') #App_Secret from developers portal

app.register_blueprint(need_routes, current_user=current_user)
app.register_blueprint(users_routes, current_user=current_user)
app.register_blueprint(pay_routes, current_user=current_user)
app.register_blueprint(hist_routes, current_user=current_user)

Session(app)

init_db(app)
migrate = Migrate(app, db)

"""User Intergrations"""
user_manager = UserManager(app, db, User)

#csrf = CSRFProtect(app)

# Once connectivity is established create the tables
with app.app_context():
    db.create_all()

"""user loader"""
login_manager = LoginManager(app)
#login_manager.login_view = 'usr_routes.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# @app.route('/google/auth')
# def google_auth():
#     authorization_url, state = flow.authorization_url()
#     session['state'] = state
#     return redirect(authorization_url)

# @app.route(GOOGLE_REDIRECT_URI)
# def google_auth_callback():
#     state = session.pop('state', None)
#     flow.fetch_token(authorization_response=request.url, state=state)
#     credentials = flow.credentials
    
   
#     id_info = id_token.verify_oauth2_token(
#         credentials.id_token, requests.Request(), GOOGLE_CLIENT_ID)
    
#     # Print user details
#     print("User ID:", id_info['sub'])
#     print("Email:", id_info['email'])
#     print("Name:", id_info['name'])
#     print("Profile Picture URL:", id_info['picture'])
    
#     return "Successfully authenticated!"

@app.route("/")
def home():
    return {"check": "Checking if the route works"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5000, debug=True)