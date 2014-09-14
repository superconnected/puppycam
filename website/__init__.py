from flask import Flask, render_template, url_for
from flask.ext.basicauth import BasicAuth
import ConfigParser
import os

app = Flask(__name__)

config = ConfigParser.RawConfigParser()
config_file = os.path.join(os.path.dirname(__file__), 'app.cfg')
config.read(config_file)

app.config['BASIC_AUTH_USERNAME'] = config.get('Auth', 'username')
app.config['BASIC_AUTH_PASSWORD'] = config.get('Auth', 'password')
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)

from website import views
