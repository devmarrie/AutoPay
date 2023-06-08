from flask import Blueprint, jsonify, request
from models.need import Need
from models.database import db

need_routes = Blueprint('need_routes', __name__)

"""Needs routes"""
@need_routes.route('/add_need', methods=['POST'])
def add_need():
    data = request.get_json()
    ned = Need(need=data['need'], amount=data['amount'], duedate=data['duedate'], reminderdate=['reminderdate'])
    db.session.add(ned)
    db.session.commit()
    return jsonify({'message': 'New need created successfully'})

