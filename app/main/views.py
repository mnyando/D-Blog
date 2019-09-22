from flask import render_template,redirect,url_for
from app.main import main
from app.requests import get_quotes

@main.route('/')
def index():
    quotes = get_quotes()
    print(quotes)
    return render_template('index.html', quote = quotes)

@main.route('/profile')
def profile():
    return render_template('profile/profile.html')