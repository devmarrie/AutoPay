from .base_model import BaseModel
from models.database import db

class History(BaseModel):
    __tablename__ = 'history'
    status = db.Column(db.String, nullable=False)
    code = db.Column(db.String, nullable=True)
    # user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)

