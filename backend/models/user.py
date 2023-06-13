from .base_model import BaseModel
from models.database import db

class User(BaseModel):
    __tablename__ = 'users'
    name = db.Column(db.String(60), nullable=False)
    phone_no = db.Column(db.String(60),  unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)
    #payments = db.relationship('Pay', backref='users')
    needs = db.relationship('Need', backref='users')