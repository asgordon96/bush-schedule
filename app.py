# The main Flask application file
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, session, flash

import os
from functools import wraps
import gmail
import models

Flask.debug = True
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'app.db'
db = SQLAlchemy(app)
app.secret_key = os.environ['FLASK_SECRET']

def require_login(f):
    @wraps(f)
    def new_function(*args, **kwargs):
        if not 'user_id' in session.keys() or not session['user_id']:
            return redirect("/")
        else:
            return f(*args, **kwargs)
    return new_function

@app.route("/")
def main():
    return render_template("login_form.html")
	
@app.route("/schedule")
@require_login
def schedule():
    if session['user_id']:
        user = models.User.query.get(session['user_id'])
        
	return render_template('schedule.html')

# routing for accounts and logins
@app.route("/account/new")
def new_account():
    return render_template("create_account.html")
    
@app.route("/account/create", methods=["POST"])
def create_account():
    # send an email the the bush.edu email address with a temp password
    if request.form['email'].endswith("@bush.edu"):
        temp_password = gmail.send_password(request.form['email'])
        new_user = models.User(request.form['email'], temp_password)
        db.session.add(new_user)
        db.session.commit()
    
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']
    user = models.User.authenticate(email, password)
    if user:
        session['user_id'] = user.id
        return redirect("/schedule")
    else:
        flash("Incorrect email or password")
        return redirect("/")

@app.route("/logout", methods=["POST"])
@require_login
def logout():
    session.pop('user_id', None)
    return redirect('/')

# routes relating to chaning user info (passwords)
@app.route("/password", methods=["GET"])
@require_login
def password_change_page():
    return render_template("change_password.html")
    
@app.route("/password", methods=["POST"])
@require_login
def change_password():
    user = models.User.query.get(session['user_id'])
    old_password = request.form["current_password"]
    new_password = request.form["new_password"]
    confirm = request.form["new_password_confirm"]
    if models.User.authenticate(user.bush_email, old_password) == user:
        if new_password == confirm:
            user.change_password(confirm)
            db.session.merge(user)
            db.session.commit()
            return "Password Changed. <a href='/schedule'>Home</a>"
        else:
            flash("Password did not match")
    else:
        flash("Incorrect Password")
    return redirect("/password")

@app.route("/classes", methods=["GET"])
@require_login
def classes_form():
    return render_template("classes_form.html")
    
@app.route("/classes", methods=["POST"])
@require_login
def add_classes():
    user = models.User.query.get(session['user_id'])
    blocks = request.form.keys()
    blocks.sort()
    for i in range(6):
        block_class = user.classes[i]
        block_class.name = request.form[blocks[i]]
        db.session.merge(block_class)
    db.session.commit()
    return redirect('/schedule')

if __name__ == "__main__":
    app.run()