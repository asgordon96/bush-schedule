# The main Flask application file
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'app.db'
db = SQLAlchemy(app)

@app.route("/")
def main():
    return "Hello Flask"
    
if __name__ == "__main__":
    app.run()