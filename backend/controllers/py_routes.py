from flask import Blueprint, jsonify, request, current_app
from models.pay import Pay
from models.database import db
from dotenv import load_dotenv
import requests
from datetime import datetime
from flask_mpesa import MpesaAPI
import os
import base64
import json

pay_routes = Blueprint('pay_routes', __name__)

load_dotenv()

"""Mpesa Intergration"""
mpesa_api = MpesaAPI(current_app)
# consumer_key = os.getenv('CONSUMER_KEY')
# consumer_secret = os.getenv('CONSUMER_SECRET')
callback_url = os.getenv('CALLBACK_URL')

"""The authentication process to obtain the access token"""
# def token():
#     mpesa_auth_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
#     response = requests.get(mpesa_auth_url, auth=(consumer_key, consumer_secret))
#     if response.status_code == 200:
#         access_token = response.json().get('access_token')
#         return access_token
#     else:
#         return "Authentication failed", 401
    
"""Register urls"""
# @pay_routes.route('/register')
# def register_urls():
#      endpoint = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
#      access_token = token()
#      headers = { "Authorization": "Bearer %s" % access_token }
#      reg_data = {
#         "ShortCode": "600383",
#         "ResponseType": "Completed",
#         "ConfirmationURL": callback_url + '/confirm',
#         "ValidationURL": callback_url + '/validate'
#     }

#      response = requests.post(endpoint, json = reg_data, headers = headers)
#      return response.json()

# @pay_routes.route('/confirm')
# def confirm():
#     data = request.get_json()
#     return data

# @pay_routes.route('/validate')
# def validate():
#     data = request.get_json()
#     return data

## simulate
# @pay_routes.route('/simulate')
# def test_payment():
#     endpoint = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate'
#     access_token = token()
#     headers = { "Authorization": "Bearer %s" % access_token }

#     data_s = {
#         "Amount": 1,
#         "ShortCode": "600383",
#         "BillRefNumber": "test",
#         "CommandID": "CustomerPayBillOnline",
#         "Msisdn": "254708374149"
#     }

#     res = requests.post(endpoint, json= data_s, headers = headers)
#     return res.json()


# @pay_routes.route('/mpesa_accesstoken', methods=['GET'])
# def authenticate():
#     data = token()
#     return data


@pay_routes.route('/new_payment')
def create_payment():
    amount = request.args.get('amount')
    mpesano = request.args.get('mpesano')

    endpoint = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    # access_token = token()
    # headers = { "Authorization": "Bearer %s" % access_token }
    Timestamp = datetime.now()
    frtime = Timestamp.strftime("%Y%m%d%H%M%S")
    raw_password = "174379" + "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919" + frtime
    password_bytes = raw_password.encode('utf-8')
    password = base64.b64encode(password_bytes).decode('utf-8')

    data = {
        "business_shortcode": "174379", 
        "passcode": password,#from developers portal
        "amount": amount, # choose amount preferrably KSH 1
        "phone_number": mpesano, #phone number to be prompted to pay
        "reference_code": "AutoPay",#Code to inform the user of services he/she is paying for.
        "callback_url": callback_url + '/stk_pay', # cllback url should be exposes. for testing putposes you can route on host 0.0.0.0 and set the callback url to be https://youripaddress:yourport/endpoint
        "description": "Test payment" #a description of the transaction its optional
    }

    resp = mpesa_api.MpesaExpress.stk_push(**data)
    return resp

"""Consume the mpesa callback """
@pay_routes.route("/stk_pay", methods=['POST'])
def incoming():
    json_data = request.get_json()
    print(json_data)
    result_code=json_data["Body"]["stkCallback"]["ResultCode"]
    message={
        "ResultCode":0,
        "ResultDesc":"success",
        "ThirdPartyTransID":"h234k2h4krhk2"
    }
    #if result code is 0 you can proceed and save the data else if its any other number you can track the transaction
    return jsonify(message),200
    # f = open('stk.json', 'a')
    # f.write(json.dump(info))
    # f.close()
    # callback_metadata = info['stkCallback']['CallbackMetadata']
    # items = callback_metadata['Item']
    # print(items)

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
    return json_data


@pay_routes.route('/b2c', methods=['GET'])
def settle_payments():
    amount = request.args.get('amount')
    mpesano = request.args.get('mpesano')
    endpoint = 'https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest'
    # access_token = token()
    # headers = { "Authorization": "Bearer %s" % access_token }
    my_url = callback_url + "/b2c/"

    data = {
            "initiator_name": "testapi364",
            "security_credential": os.getenv('SECURITY_CREDENTIALS'),
            "amount": "1",
            "command_id":"BusinessPayment",
            "party_a": "600364",
            "party_b": mpesano,
            "remarks": "Need paid successfully",
            "queue_timeout_url": my_url + "timeout" ,
            "result_url": my_url + "result",
            "occassion": "Need"
    }

    # res = mpesa_api.B2C.transact(**data)
    # return res.json()

    res = mpesa_api.B2C.transact(**data)
    return res

@pay_routes.route('/b2c/timeout', methods=['POST'])
def b2c_timeout():
    data = request.get_json()
    print(data)
    return "ok"


@pay_routes.route('/b2c/result', methods=['POST'])
def b2c_result():
    data = request.get_json()
    print(data)
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