from flask import render_template,redirect,url_for,abort
from app.main import main
from app.models import User,Blog
from .forms import UpdateProfile,CreateBlog
from .. import db
from app.requests import get_quotes
from flask_login import login_required,current_user

@main.route('/')
def index():
    quotes = get_quotes()
    blogs = Blog.query.order_by(Blog.posted.desc()).limit(3).all()
    return render_template('index.html', quote = quotes,blogs=blogs)

@main.route('/profile/<name>')
@login_required
def profile(name):
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
   
    return render_template('profile/profile.html',user = user)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/updateprofile.html',form =form)


@main.route('/new_post', methods=['POST','GET'])
@login_required
def new_blog():
    form = CreateBlog()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id =  current_user._get_current_object().id
        blog = Blog(title=title,content=content,user_id=user_id)
        blog.save()
        return redirect(url_for('main.index'))
    return render_template('newblog.html', form = form)