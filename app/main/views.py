from flask import render_template,redirect,url_for,abort,request
from . import main
from .. import db
from ..models import Blog,User,Comments
from flask_login import login_required,current_user
from ..request import get_quotes
from .forms import Blogform

@main.route('/')
def index():

    title = 'Welcome'
    return render_template('index.html',title=title)

@main.route('/new/blog',methods=["GET","POST"])
@login_required
def new_blog():
    blog_form = Blogform()

    if blog_form.validate_on_submit():
        blog_title = blog_form.blog_title.data
        blog_content = blog_form.content.data
        category = blog_form.category.data

        new_blog = Blog(blog_title=blog_title,blog_content=blog_content,category=category,user=current_user)
        new_blog.save_blog()

        return redirect(url_for('.index'))

    quote = get_quotes()
        
    title = 'New Blog post'

    return render_template('new_blog.html',title=title,blog_form=blog_form,quote=quote)