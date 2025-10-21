from models.daily_diet_db import db
from datetime import datetime

class Diet(db.Model):
    __tablename__ = "diets"
    #id, name, description, date-time, following the diet?
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    description = db.Column(db.String(180), nullable = True, default="")
    date_time = db.Column(db.DateTime(), nullable = False, default=datetime.utcnow)
    f_diet = db.Column(db.Boolean(), nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="diets")
    #foreignKey, chave estrangeira utilizada para referenciar tabelas


