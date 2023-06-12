from flask import Blueprint, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
from models.need import Need
from models.user import User
from models.database import db
from datetime import datetime, timedelta
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
    duedate = datetime.strptime(data['duedate'], '%H:%M:%S %d-%m-%Y')
    storable_date = duedate.strftime('%Y-%m-%d %H:%M:%S')
    user_id = data['user_id']
    history_id = data['history_id']

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    ned = Need(need=need, amount=amount, duedate=storable_date,
               user_id=user_id, history_id=history_id )
    

    parsed_number = phonenumbers.parse(user.phone_no, None)
    formatted_no = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

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