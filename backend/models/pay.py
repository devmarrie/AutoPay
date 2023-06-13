from .base_model import BaseModel
from models.database import db

class Pay(BaseModel):
    __tablename__ = 'pay'
    amount = db.Column(db.Integer(), nullable=False)
    mpesa_receipt_number = db.Column(db.String(100), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    mpesano = db.Column(db.Integer(), nullable=False)
    #user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)