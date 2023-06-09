from flask import Blueprint, jsonify, request
from models.need import Need
from models.user import User
from models.pay import Pay
from models.history import History
from models.database import db

need_routes = Blueprint('need_routes', __name__)
users_routes = Blueprint('user_routes', __name__)
pay_routes = Blueprint('pay_routes', __name__)
hist_routes = Blueprint('hist_routes', __name__)

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

"""Pay routes"""
@pay_routes.route('/new_payment', methods=['POST'])
def create_payment():
    data = request.get_json()
    amount = data['amount']
    mpesano = data['mpesano']
    user_id = data['user_id']
    p = Pay(amount=amount, mpesano=mpesano, user_id=user_id)
    db.session.add(p)
    db.session.commit()
    return jsonify({'message': 'Payment created succesfully'})

"""History routes"""
@hist_routes.route('/new_history', methods=['POST'])
def create_history():
    data = request.get_json()
    status = data['status']
    code = data['code']
    h = History(status=status, code=code)
    db.session.add(h)
    db.session.commit()
    return jsonify({'message': 'History created succesfully'})

"""Needs routes"""
@need_routes.route('/add_need', methods=['POST'])
def add_need():
    data = request.get_json()
    need = data['need']
    amount = data['amount']
    duedate = data['duedate']
    reminderdate = data['reminderdate']
    ned = Need(need=need, amount=amount, duedate=duedate, reminderdate=reminderdate)
    db.session.add(ned)
    db.session.commit()
    return jsonify({'message': 'New need created successfully'})


@need_routes.route('/get_needs')
def get_needs():
    needs =  Need.query.all()
    return jsonify([n.to_dict() for n in needs])

@need_routes.route('/update_need/<string:id>', methods=['PUT'])
def update_need(id):
    need = Need.query.get(id)
    if not need:
        return jsonify({'error': 'Need not found' }), 404
    data = request.get_json()
    need.need = data.get('need', need.need)
    need.amount = data.get('amount', need.amount)
    need.duedate = data.get('duedate', need.duedate)
    need.reminderdate = data.get('reminderdate', need.reminderdate)
    db.session.commit()
    return jsonify(need.to_dict())

@need_routes.route('/delete_need/<string:id>', methods=['DELETE'])
def del_need(id):
    n = Need.query.get(id)
    if n:
        db.session. delete(n)
        db.session.commit()
        return jsonify({'message': f'Need belonging to {id} deleted successfully'})
    else:
        return jsonify({'error': f'Need with {id} not found'}), 404