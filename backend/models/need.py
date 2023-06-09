from .base_model import BaseModel
from models.database import db

class Need(BaseModel):
    __tablename__ = 'needs'
    need = db.Column(db.String(50), unique=True, nullable=False)
    amount = db.Column(db.Integer(), nullable=False)
    duedate = db.Column(db.DateTime, nullable=False)
    reminderdate = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    history_id = db.Column(db.String(60), db.ForeignKey('history.id'), nullable=False)

