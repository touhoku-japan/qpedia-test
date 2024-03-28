import constants as c

import os
from flask import render_template, request, redirect, url_for, session
from functools import wraps
## Flask related Front-End functions

# Login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

@c.app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != os.environ["APPLICATION_ADMIN_ACCOUNT"] or request.form['password'] != os.environ["APPLICATION_ADMIN_ACCOUNT_PW"]: #Change
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@c.app.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@c.app.route('/')
@login_required
def index():
    return render_template('index.html')
