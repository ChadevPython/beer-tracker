# -*- coding: utf-8 -*-

import logging
from flask import Flask
from config import config
from flask_user import UserManager, SQLAlchemyAdapter
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

app = Flask(__name__)
app.secret_key = config.APP_SECRET_KEY
app.config['SECRET_KEY'] = config.APP_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = config.DEBUG

app.config['MAIL_SERVER'] = config.MAIL_SERVER
app.config['MAIL_PORT'] = config.MAIL_PORT
app.config['MAIL_USE_TLS'] = config.MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = config.MAIL_USE_SSL
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = config.MAIL_DEFAULT_SENDER

mail = Mail(app)
db = SQLAlchemy(app)

# Setup Flask-User
from tracker.models.user import User
db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
user_manager = UserManager(db_adapter, app)     # Initialize Flask-User
user_manager.app_name = config.APP_NAME

if not app.debug:
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.basicConfig(filename='error.log', level=logging.INFO, format='%(asctime)s %(message)s')

# custom jinja line delimeters
app.jinja_env.line_statement_prefix = '%'
app.jinja_env.line_comment_prefix = '##'

from tracker.views import init_views
init_views(app)
