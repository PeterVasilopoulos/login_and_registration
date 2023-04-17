from flask import render_template, request, redirect, session

from login_app.models.users_model import User

from login_app import app

# Default page renders login page
@app.route('/')
def default():
    return render_template('login_page.html')

# Login route
@app.route('/login', methods = ["POST"])
def login():
    logged_in_user = User.login(request.form)

    if logged_in_user:
        session['uid'] = logged_in_user.id
        return redirect('/dashboard')
    else:
        return redirect('/')

# Register route
@app.route('/register', methods = ["POST"])
def register():
    validate_reg = User.register(request.form)

    if validate_reg:
        session['uid'] = User.create(request.form)
        return redirect('/dashboard')
    else:
        return redirect('/')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if not 'uid' in session:
        return redirect('/')

    return render_template('dashboard.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')