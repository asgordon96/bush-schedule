# The Main Database Models
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bush_email = db.Column(db.String(100), index=True, unique=True)
    grade = db.Column(db.Integer)
    password_hash = db.Column(db.String(256))