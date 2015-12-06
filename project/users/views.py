from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from app import app
from flask.ext.bcrypt import Bcrypt
from functools import wraps

bcrypt = Bcrypt(app)

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            flash('Invalid credentials.')
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template("login.html")

@users_blueprint.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    print('APP_SETTINGS set to', os.environ['APP_SETTINGS'])
    print('DATABASE_URI set to', os.environ['DATABASE_URL'])
    app.run()
