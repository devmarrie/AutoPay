from .base_model import BaseModel
from models.database import db

class Pay(BaseModel):
    __tablename__ = 'pay'
    amount = db.Column(db.Integer(), nullable=False)
    mpesano = db.Column(db.Integer(), nullable=False)