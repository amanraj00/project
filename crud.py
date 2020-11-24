"""CRUD.py"""

from model import db, User, Movie, Rating, connect_to_db

def create_user(first_name, last_name, email_address, password): 
    """Create new user."""

    new_user = User(first_name = first_name, last_name = last_name, email_address = email_address, password = password)

    db.session.add(new_user)
    db.session.commit()

    return new_user

alia = create_user('Alia','Manraj','amanraj@gmail.com','Alia123')
jane = create_user('Jane','Doe','janedoe@noemail.com','Jane123')
john = create_user('John','Smith','johnsmith@noemail.com','John123')

def user_entry(text, user)
    """User's gratitude entry."""

    entry = GratitudeEntries(text = text, user = user)

    db.session.add(entry)
    db.session.commit()

    return entry

aentry = GratitudeEntries(text = 'My advisor', user = alia)
bentry = GratitudeEntries(text = 'My home', user = jane)
centry = GratitudeEntries(text = 'Coffee', user = john)

def motivational_message(text, credit)
    """Quote that's rewarded after entry."""

    motivation = Quotes(text = text, credit = credit)

    db.session.add(motivation)
    db.session.commit()

    return motivation 

q1 = Quotes(text = 'If we have the atittude that it is going to be a great day, it usually is.', credit = 'Catherine Pulsifier')
q2 = Quotes(text = 'Your passion is waiting for your courage to catch up.', credit = 'Isabelle Lafleche')
q3 = Quotes(text = 'Work in silence, let your success be the noise.', credit = 'Frank Ocean') 