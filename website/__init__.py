from flask import Flask, render_template, url_for
from flask.ext.basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'xxxx'
app.config['BASIC_AUTH_PASSWORD'] = 'xxxx'
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)

from website import views
