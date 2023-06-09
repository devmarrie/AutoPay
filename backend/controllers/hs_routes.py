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

@hist_routes.route('/update_history/<string:id>', methods=['PUT'])
def update_history(id):
    hist = History.query.get(id)
    if not hist:
        return jsonify({'error': 'History record not found' }), 404
    data = request.get_json()
    hist.status = data.get('status', hist.status)
    hist.code = data.get('code', hist.code)
    db.session.commit()
    return jsonify(hist.to_dict())

@hist_routes.route('/delete_history/<string:id>', methods=['DELETE'])
def del_history(id):
    h = History.query.get(id)
    if h:
        db.session. delete(h)
        db.session.commit()
        return jsonify({'message': f'Payment history belonging to {id} deleted successfully'})
    else:
        return jsonify({'error': f'Payment history with {id} not found'}), 404