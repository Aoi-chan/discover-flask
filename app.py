from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from functools import wraps

app = Flask(__name__)
bcrypt = Bcrypt(app)

import os
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

app.register_blueprint(users_blueprint)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

if __name__ == '__main__':
    print('APP_SETTINGS set to', os.environ['APP_SETTINGS'])
    print('DATABASE_URI set to', os.environ['DATABASE_URL'])
    app.run()
