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
        return f'<User first_name={self.first_name} last_name={self.last_name} email={self.email_address}>'

class GratitudeEntries(db.Model):
    """Things user is grateful for."""

    __tablename__ = 'entries'

    entry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    date = db.Column(db.DateTime)
    user = db.relationship('User', backref='entries')

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

    
# fred = User(first_name = 'Fred', last_name = 'Flinstone', email_address = 'fredemail@email.com', password = 'Fred123')

def connect_to_db(flask_app, db_uri='postgresql:///positivity', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    # from server import app
    from flask import Flask
    app = Flask(__name__)
    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)