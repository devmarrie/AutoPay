from flask import Blueprint, jsonify, request, redirect, url_for
from models.user import User
from models.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from flask_user import current_user, login_required, roles_required, roles_accepted

users_routes = Blueprint('user_routes', __name__)

"""Users routes"""
@users_routes.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return jsonify({"message": "User Authenticated"})
        # return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form['username']
        unhashed = request.form['password']
        phone_no = request.form['phone_no']

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
        username = request.form['username']
        password = request.form['password']
    
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
           login_user(user)
           return jsonify({'message': 'User logged in successfully'})
        else:
            return jsonify({'error': 'Invalid credentials'}), 401

@users_routes.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'User logged out successfully'})

@users_routes.route('/get_users')   
def get_users():
    users =  User.query.all()
    return jsonify([user.to_dict() for user in users])


@users_routes.route('/update_user/<string:id>', methods=['PUT'])
def update_user(id):
    us = User.query.get(id)
    if not us:
        return jsonify({'error': 'User not found' }), 404
    data = request.get_json()
    us.name = data.get('name', us.name)
    us.phone_no = data.get('phone_no', us.phone_no)
    us.password = data.get('password', us.password)
    db.session.commit()
    return jsonify(us.to_dict())    

@users_routes.route('/delete_user/<string:id>', methods=['DELETE'])
def del_need(id):
    u = User.query.get(id)
    if u:
        db.session. delete(u)
        db.session.commit()
        return jsonify({'message': f'User belonging to {id} deleted successfully'})
    else:
        return jsonify({'error': f'User with {id} not found'}), 404