from flask import Blueprint, jsonify, request
from models.need import Need
from models.database import db
from datetime import datetime

need_routes = Blueprint('need_routes', __name__)


"""Needs routes"""
@need_routes.route('/add_need', methods=['POST'])
def add_need():
    data = request.get_json()
    need = data['need']
    amount = data['amount']
    duedate = datetime.strptime(data['duedate'], '%H:%M %d-%m-%Y')
    storable_date = duedate.strftime('%Y-%m-%d %H:%M')
    user_id = data['user_id']
    history_id = data['history_id']
    ned = Need(need=need, amount=amount, duedate=storable_date,
               user_id=user_id, history_id=history_id )
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