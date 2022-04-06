from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Creating a Flask instance
app = Flask(__name__)
# Setting up a secret key
app.config["SECRET_KEY"] = "9cac665aaa015830e2eecc9977977f68"
# Adding Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# Initializing database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from flaskblog import routes