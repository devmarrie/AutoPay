from flask import Blueprint, jsonify, request, redirect, url_for
from models.user import User
from models.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from flask_user import current_user, login_required, current_app
from flask import session


users_routes = Blueprint('user_routes', __name__)


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
        

@users_routes.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return jsonify({"message": "User Authenticated"})
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        password = data['password']
    
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
           login_user(user, remember=True)
           return jsonify({'message': 'User logged in successfully'})
           #return redirect('http://localhost:3000/needs')
        #    session_cookie_name = session_manager.session_cookie_name
        #    session_id = request.cookies.get(session_cookie_name)
        #    response = jsonify({'message': 'User logged in successfully'})
        #    response.set_cookie(current_app.config['SESSION_COOKIE_NAME'], session_id)
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
        # session_cookie = request.headers.cookies.get('id')
        

@users_routes.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'User logged out successfully'})

@users_routes.route('/view_profile') 
@login_required  
def view_profile():
    user = current_user
    return jsonify({
        'username': user.username,
        'phone_no': user.phone_no
    })


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