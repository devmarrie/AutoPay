from flask import Blueprint, jsonify, request
from models.user import User
from models.database import db

users_routes = Blueprint('user_routes', __name__)

"""Users routes"""
@users_routes.route('/new_user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    usr = User(name=name, email=email, password=password)
    db.session.add(usr)
    db.session.commit()
    return jsonify({'message': 'User created succesfully'})

@users_routes.route('/get_users')   
def get_users():
    users =  User.query.all()
    return jsonify([user.to_dict() for user in users])
