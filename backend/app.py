from flask import Flask,session,redirect, request, jsonify
from models.database import db, init_db
from flask_migrate import Migrate
from flask_user import UserManager
from flask_login import LoginManager, current_user, login_required
from dotenv import load_dotenv
from models.user import User
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_session import Session
from controllers import need_routes, users_routes, pay_routes, hist_routes
import os
import secrets
import redis

#google auth
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

app = Flask(__name__)
app.secret_key = GOOGLE_CLIENT_SECRET
CORS(app, origins=['http://localhost:3000'], 
     methods=['GET', 'POST', 'PUT', 'DELETE'], 
     headers=['Content-Type', 'Authorization'],
    supports_credentials=True
    )

load_dotenv()
# Db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')
app.config['USER_EMAIL_SENDER_EMAIL'] = os.getenv('EMAIL')
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLACHEMY_ECHO'] = True
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SESSION_TYPE'] = 'filesystem'

"""Session config"""
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url('redis://127.0.0.1:6379')


"""Mpesa Intergration"""
app.config["API_ENVIRONMENT"] = "sandbox" #sandbox or production
app.config["APP_KEY"] = os.getenv('CONSUMER_KEY')# App_key from developers portal
app.config["APP_SECRET"] = os.getenv('CONSUMER_SECRET') #App_Secret from developers portal

Session(app)

init_db(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)
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


app.register_blueprint(users_routes)
app.register_blueprint(need_routes)
app.register_blueprint(pay_routes)
app.register_blueprint(hist_routes)

@app.route("/sign-in", methods=['POST'])
def signin():
    username = request.json["username"]
    password = request.json["password"]
    email = request.json["email"]

    user_exists = User.query.filter_by(username=username).first() is not None

    if user_exists:
        return jsonify({
            "error": "User Already exists"
        }), 409
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username,password=hashed_password, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id,
        "username": new_user.username
    })

@app.route("/login", methods=['POST'])
def login():
    username = request.json["username"]
    password = request.json["password"]

    user = User.query.filter_by(username=username).first()

    if user is None:
        return jsonify({
            "error": "User not found in db"
        }), 401
    if not bcrypt.check_password_hash(user.password.encode('utf-8'), password):
        return jsonify({
            "error": "Passwords do not match"
        }), 401
    
    session["user_id"] = user.id

    return jsonify({
        "id": user.id,
        "username": user.username
    })

@app.route("/details", methods=['GET'])
def view_details():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({
            "error": "Unathorized"
        }), 401
    
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return jsonify({
            "error": "User not found"
        }), 404

    return jsonify({
        "id": user.id,
        "username": user.username
    })

@app.route('/update_usr/<string:username>', methods=['PUT'])
def update_need(username):
    usr = User.query.filter_by(username=username).first()
    if not usr:
        return jsonify({'error': 'User not found' }), 404
    data = request.get_json()
    usr.username = data.get('username', usr.username)
    usr.email = data.get('email', usr.email)
    usr.password = data.get('password', usr.password)
    db.session.commit()
    return jsonify(usr.to_dict())

# """Needs"""
# # Africas Talking credentials
# username = 'sandbox'
# api_key = '710e7cbe8961305d6c90cfbf2bdf1abbad728e3405eb75da0c967c9225d73938'
# africastalking.initialize(username, api_key)
# sms = africastalking.SMS

# # Function to send sms
# def send_sms(to, message):
#     try:
#         response = sms.send(message, [to])
#         print(response)
#     except Exception as e:
#         print(f'An error occoured while sending message {e}')

# """Needs routes"""
# @app.route('/add_need', methods=['POST'])
# def add_need():
#     data = request.get_json()
#     need = data['need']
#     amount = data['amount']
#     duedate = datetime.strptime(data['duedate'], '%H:%M:%S %d-%m-%Y')
#     storable_date = duedate.strftime('%Y-%m-%d %H:%M:%S')

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
#     user_id = user.id

#     ned = Need(need=need, amount=amount, duedate=storable_date,
#                user_id=user_id)
    

#     try:
#         parsed_number = phonenumbers.parse(user.phone_no, "KE")
#         formatted_no = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
#     except NumberParseException as e:
#         return jsonify({
#             "error": f"Invalid phone number: {e}"
#         }), 400

#     def send_three_minutes_before():
#         send_sms(formatted_no, f'The payment for {need} is due soon')

#     def send_on_due_date():
#         send_sms(formatted_no, f'The {need} should be settled today')

#     def send_two_minutes_after():
#        send_sms(formatted_no, f'The payment for {need} has been delayed by two minutes')

#     # Background scheduler
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(send_three_minutes_before, 'date', run_date=duedate - timedelta(minutes=3))
#     scheduler.add_job(send_on_due_date, 'date', run_date=duedate)
#     scheduler.add_job(send_two_minutes_after, 'date', run_date=duedate + timedelta(minutes=2))
#     scheduler.start()

#     db.session.add(ned)
#     db.session.commit()

#     return jsonify({'message': 'New need created successfully'})

@app.route("/")
def home():
    return {"check": "Checking if the route works"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5000, debug=True)