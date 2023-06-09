from flask import Blueprint, jsonify, request
from models.pay import Pay
from models.database import db

pay_routes = Blueprint('pay_routes', __name__)

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

@pay_routes.route('/get_pay')   
def get_pay():
    pm =  Pay.query.all()
    return jsonify([p.to_dict() for p in pm])
