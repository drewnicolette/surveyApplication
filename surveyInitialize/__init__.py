#Intialize Application and bring together components
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Knows where to look for template and static files
app = Flask(__name__)

#Set secret key
app.config['SECRET_KEY'] = '123456789'

#This site.db is a database file where we are going to stored database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#Database instance, sending this to models.py
db = SQLAlchemy(app)

from surveyInitialize import routes

#To get started - Run: export FLASK_APP=frontEnd.py
#To move to debug mode - Run: export FLASK_DEBUG=1
#To start web server - flask run