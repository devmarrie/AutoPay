from .base_model import BaseModel
from models.database import db
from flask_user import UserMixin

class User(BaseModel, UserMixin):
    __tablename__ = 'users'
    username = db.Column(db.String(60), nullable=False)
    phone_no = db.Column(db.String(60),  unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)
    #payments = db.relationship('Pay', backref='users')
    needs = db.relationship('Need', backref='users')