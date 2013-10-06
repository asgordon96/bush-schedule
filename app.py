# The main Flask application file
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'app.db'
db = SQLAlchemy(app)

@app.route("/")
def main():
    return "Hello Flask"
	
@app.route("/schedule")
def schedule():
	return render_template('schedule.html')
    
if __name__ == "__main__":
    app.run()