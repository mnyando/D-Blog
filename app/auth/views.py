from flask import render_template, redirect,url_for
from app.auth import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')

