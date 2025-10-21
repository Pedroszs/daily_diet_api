from models.daily_diet_db import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "user"
    #id, username and password
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable= False, unique = True)
    password = db.Column(db.String(80), nullable= False)
    role =  db.Column(db.String(80), nullable = False, default ="user")
    diets = db.relationship("Diet", back_populates="user", lazy=True)
    #relationship, criar relações entre as tabelas.