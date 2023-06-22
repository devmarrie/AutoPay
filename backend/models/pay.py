from .base_model import BaseModel
from models.database import db

class Pay(BaseModel):
    __tablename__ = 'pay'
    amount = db.Column(db.Integer(), nullable=False)
    number = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(100), nullable=False)
    need = db.Column(db.String(60), nullable=False)
    #user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)