# The Main Database Models
import bcrypt
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bush_email = db.Column(db.String(100), index=True, unique=True)
    grade = db.Column(db.Integer)
    password_hash = db.Column(db.String(256))
    
    @classmethod
    def authenticate(cls, email, password):
        user = User.query.filter_by(bush_email=email).first()
        if user:
            if bcrypt.hashpw(password, user.password_hash) == user.password_hash:
                return user
        return False
    
    def __init__(self, email, password, grade=None):
        self.bush_email = email
        self.password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
        if grade:
            self.grade = grade
        
    