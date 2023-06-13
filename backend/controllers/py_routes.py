from flask import Blueprint, jsonify, request
from models.pay import Pay
from models.database import db
import requests
from datetime import datetime
import base64

pay_routes = Blueprint('pay_routes', __name__)

# mpesa details
consumer_key = 'b3G7K3Rr7TMaJiOXfeoBW97R71aN7uC9'
consumer_secret = 'X3qaq8XnvnfFJXcm'
callback_url = 'https://90fc-197-232-61-203.ngrok-free.app'

"""The authentication process to obtain the access token"""
def token():
    mpesa_auth_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(mpesa_auth_url, auth=(consumer_key, consumer_secret))
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        return access_token
    else:
        return "Authentication failed", 401

@pay_routes.route('/mpesa_accesstoken', methods=['GET'])
def authenticate():
    data = token()
    return data


@pay_routes.route('/new_payment')
def create_payment():
    amount = request.args.get('amount')
    mpesano = request.args.get('mpesano')

    endpoint = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    access_token = token()
    headers = { "Authorization": "Bearer %s" % access_token }
    Timestamp = datetime.now()
    frtime = Timestamp.strftime("%Y%m%d%H%M%S")
    raw_password = "174379" + "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919" + frtime
    password_bytes = raw_password.encode('utf-8')
    password = base64.b64encode(password_bytes).decode('utf-8')

    data = {
        "BusinessShortCode": "174379",    
        "Password": password,    
        "Timestamp": frtime,    
        "TransactionType": "CustomerPayBillOnline",    
        "Amount": amount,    
        "PartyA": mpesano,    
        "PartyB":"174379",    
        "PhoneNumber": mpesano,    
        "CallBackURL": callback_url + "/stk_pay",    
        "AccountReference":"TestPay",    
        "TransactionDesc":"Test payment"
    }

    res = requests.post(endpoint, json=data, headers=headers)
    return res.json()

"""Consume the mpesa callback """
@pay_routes.route("/stk_pay", methods=['POST'])
def incoming():
    info = request.get_json()['Body']
    callback_metadata = info['stkCallback']['CallbackMetadata']
    items = callback_metadata['Item']
    print(items)

    # for item in items:
    #     if item['Name'] == 'Amount':
    #         amount = item['Value']
    #     elif item['Name'] == 'MpesaReceiptNumber':
    #         mpesa_receipt_number = item['Value']
    #     elif item['Name'] == 'TransactionDate':
    #         date = item['Value']
    #         strip_time = datetime.strptime(date, '%Y%m%d%H%M%S')
    #         transaction_date = strip_time.strftime('%Y-%m-%d %H:%M:%S')
    #     elif item['Name'] == 'PhoneNumber':
    #        phone_number = item['Value']

    # p = Pay(amount=amount, mpesa_receipt_number=mpesa_receipt_number,
    #          transaction_date=transaction_date, mpesano=phone_number)
    # db.session.add(p)
    # db.session.commit()
    return "ok"

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