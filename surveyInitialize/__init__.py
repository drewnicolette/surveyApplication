#Intialize Application and bring together components
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from datetime import datetime

#Knows where to look for template and static files
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789' #Set secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #This site.db is a database file where we are going to stored database
db = SQLAlchemy(app) #Database instance, sending this to models.py
bcrypt = Bcrypt(app) #For hashing passwords
login_manager = LoginManager(app) #For logins, it will handles sessions
login_manager.login_view = 'hello' #Directed hello function which is our login page
login_manager.login_message_category = 'info' #Blue information alert


from surveyInitialize import routes

#To get started - Run: export FLASK_APP=frontEnd.py
#To move to debug mode - Run: export FLASK_DEBUG=1
#To start web server - flask run