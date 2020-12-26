from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#___ not so secret key
app.config['SECRET_KEY'] = 'asjldhfalkjsdhfjashdljfkha'

#___ Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#___ Database instance
db = SQLAlchemy(app)

from flaskblog import routes