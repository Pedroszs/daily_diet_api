from models.daily_diet_db import db

class User(db.Model):
    #id, username and password
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable= False, unique = True)
    password = db.Column(db.String(80), nullable= False)
    role =  db.Column(db.String(80), nullable = False, default ="user")