from flask import Blueprint, jsonify, request
from models.pay import Pay
from models.database import db
import requests

pay_routes = Blueprint('pay_routes', __name__)

consumer_key = 'b3G7K3Rr7TMaJiOXfeoBW97R71aN7uC9'
consumer_secret = 'X3qaq8XnvnfFJXcm'

"""The authentication process to obtain the access token"""
def token():
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(api_url, auth=(consumer_key, consumer_secret))
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        return access_token
    else:
        return "Authentication failed", 401

@pay_routes.route('/mpesa_accesstoken', methods=['GET'])
def authenticate():
    data = token()
    return data

    

    


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

@pay_routes.route('/update_pay/<string:id>', methods=['PUT'])
def update_pay(id):
    pym = Pay.query.get(id)
    if not pym:
        return jsonify({'error': 'Payment not found' }), 404
    data = request.get_json()
    pym.amount = data.get('amount', pym.amount)
    pym.mpesano = data.get('mpesano', pym.mpesano)
    pym.user_id = data.get('user_id', pym.user_id)
    db.session.commit()
    return jsonify(pym.to_dict())

@pay_routes.route('/delete_pay/<string:id>', methods=['DELETE'])
def del_pay(id):
    p = Pay.query.get(id)
    if p:
        db.session. delete(p)
        db.session.commit()
        return jsonify({'message': f'Payment belonging to {id} deleted successfully'})
    else:
        return jsonify({'error': f'Payment with {id} not found'}), 404