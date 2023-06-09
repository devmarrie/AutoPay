from flask import Blueprint, jsonify, request
from models.history import History
from models.database import db

hist_routes = Blueprint('hist_routes', __name__)

"""History routes"""
@hist_routes.route('/new_history', methods=['POST'])
def create_history():
    data = request.get_json()
    print(data)
    status = data['status']
    code = data['code']
    h = History(status=status, code=code)
    db.session.add(h)
    db.session.commit()
    return jsonify({'message': 'History created succesfully'})

@hist_routes.route('/get_history')   
def get_hist():
    hist =  History.query.all()
    return jsonify([h.to_dict() for h in hist])