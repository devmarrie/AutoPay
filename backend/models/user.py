from .base_model import BaseModel
from models.database import db

class User(BaseModel):
    __tablename__ = 'users'
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120),  unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    