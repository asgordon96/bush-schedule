# The main Flask application file
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect

import gmail
import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'app.db'
db = SQLAlchemy(app)

@app.route("/")
def main():
    return render_template("login_form.html")
	
@app.route("/schedule")
def schedule():
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
        return redirect("/schedule")
    else:
        return redirect("/")    

if __name__ == "__main__":
    app.run()