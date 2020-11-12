from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User information."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email_address = db.Column(db.String, unique=True, nullable=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User first_name={self.first_name} last_name={self.last_name} email={self.email}>'

 class Gratitude_Entries(db.Model):
    """Things user is grateful for."""

    __tablename__ = 'entries'

    entry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Gratitude_Entries entry_id={self.entry_id} user_id={self.user_id}>'

class Quotes(db.Model): 
    """Positive quote for the day.""" 

    __tablename__ = 'quote'
    
    quote_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text = db.Column(db.String, unique=True)
    credit = db.Column(db.String)
    image_url = db.Column(db.String)

    def __repr__(self): 
        return f'<Quotes quote_id={self.quote_id} text={self.text}>'