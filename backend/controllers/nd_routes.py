from flask import Blueprint, jsonify, request, session
from models.database import db
from models.user import User
from apscheduler.schedulers.background import BackgroundScheduler
from phonenumbers.phonenumberutil import NumberParseException
from models.need import Need
from datetime import datetime, timedelta
from flask_user import current_user
import africastalking
import phonenumbers

need_routes = Blueprint('need_routes', __name__)


# Africas Talking credentials
username = 'sandbox'
api_key = '710e7cbe8961305d6c90cfbf2bdf1abbad728e3405eb75da0c967c9225d73938'
africastalking.initialize(username, api_key)
sms = africastalking.SMS

# Function to send sms
def send_sms(to, message):
    try:
        response = sms.send(message, [to])
        print(response)
    except Exception as e:
        print(f'An error occoured while sending message {e}')

"""Needs routes"""
@need_routes.route('/add_need', methods=['POST'])
def add_need():
    data = request.get_json()
    need = data['need']
    amount = data['amount']
    phone_no = data['phone_no']
    duedate = datetime.strptime(data['duedate'], '%H:%M:%S %d-%m-%Y')
    storable_date = duedate.strftime('%Y-%m-%d %H:%M:%S')

    # user_id = session.get("user_id")
    # if not user_id:
    #     return jsonify({
    #         "error": "Unathorized"
    #     }), 401
    
    # user = User.query.filter_by(id=user_id).first()
    # if user is None:
    #     return jsonify({
    #         "error": "User not found"
    #     }), 404
    # user_id = user.id

    ned = Need(need=need, amount=amount, duedate=storable_date,
               phone_no=phone_no)
    

    try:
        parsed_number = phonenumbers.parse(phone_no, "KE")
        formatted_no = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
    except NumberParseException as e:
        return jsonify({
            "error": f"Invalid phone number: {e}"
        }), 400

    def send_three_minutes_before():
        send_sms(formatted_no, f'The payment for {need} is due soon')

    def send_on_due_date():
        send_sms(formatted_no, f'The {need} should be settled today')

    def send_two_minutes_after():
       send_sms(formatted_no, f'The payment for {need} has been delayed by two minutes')

    # Background scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_three_minutes_before, 'date', run_date=duedate - timedelta(minutes=3))
    scheduler.add_job(send_on_due_date, 'date', run_date=duedate)
    scheduler.add_job(send_two_minutes_after, 'date', run_date=duedate + timedelta(minutes=2))
    scheduler.start()

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