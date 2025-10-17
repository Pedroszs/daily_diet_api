from models.daily_diet_db import db
from datetime import datetime

class Diet(db.Model):
    #id, name, description, date-time, following the diet?
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    description = db.Column(db.String(180), nullable = True, default="")
    date_time = db.Column(db.DateTime(), nullable = False, default=datetime.utcnow)
    f_diet = db.Column(db.Boolean(), nullable = True)

