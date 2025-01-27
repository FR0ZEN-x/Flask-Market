from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__) # Creating an instance of the Flask class to create the Flask(WSGI) application


# Configuration is a way to set up the Flask application. It is a way to tell the Flask application about the database, the secret key, and other important settings.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # Database URI to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # To suppress the warning message
app.config['SECRET_KEY'] = 'b6f5c1c3b9c7b6f5c1c3b9c7' # Secret key to protect the form data

db = SQLAlchemy(app) # Creating an instance of the SQLAlchemy class to create the database object and links with flask app.
bcrypt= Bcrypt(app) # Creating an instance of the Bcrypt class to create the bcrypt object and links with flask app.
login_manager = LoginManager(app) # Creating an instance of the LoginManager class to create the login_manager object and links with flask app.
login_manager.login_view = "login_page" # Setting the login_view attribute to redirect the user to the login_page if the user is not logged in.
login_manager.login_message_category = "info" # Setting the login_message_category attribute to display the message in the info category.
# Importing routes
from market import routes