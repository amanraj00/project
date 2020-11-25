"""Server for positivity app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
# from model import connect_to_db
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)


@app.route('/')
def homepage():
    """Access homepage."""

    return render_template('homepage.html')


@app.route('/login', methods = ['POST'])
def login():
    """Login form."""


    email = request.form.get('email') 
    password = request.form.get('password')
    print("\n\npassword = ", password)
    user = crud.get_user_by_email(email)
    print("********", user.password, "that was user.password \n\n\n")
    if user.password == password:
        return 'successfully logged in'
    print(user)
    return 'password is incorrect'


@app.route('/existingentries/<user_id>')
def all_entries(user_id):
    """Display all existing entries from user."""

    user = crud.get_user_by_user_id(user_id)
    entries = user.entries

    return render_template('entries.html', entries = entries)

if __name__ == '__main__':
    crud.connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)