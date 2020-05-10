from flask import render_template,redirect,url_for,abort,request
from . import main
from .. import db
from ..models import Blog,User,Comments
from flask_login import login_required,current_user
from ..request import get_quotes
from .forms import Blogform,UpdateForm,CommentForm,ResetPassword,ResetPasswordRequest
from ..email import send_reset_email

@main.route('/')
def index():

    blogs = Blog.query.all()

    title = 'Welcome'
    return render_template('index.html',title=title,blogs=blogs)

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

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    blogs = Blog.get_users_blogs(uname)

    if user is None:
        abort(404)

    title = 'Profile information'
    return render_template('profile/profile.html',title=title,user=user,blogs=blogs)

@main.route('/user/<uname>/update',methods=["GET","POST"])
@login_required
def update_profile(uname):
    user = User.query.user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    update = UpdateForm()

    if update.validate_on_submit():
        user.bio = update.bio.data
        user.first_name = update.first_name.data
        user.last_name = update.last_name.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username,user=user))
    
    title = 'Update profile'
    return render_template('profile/update.html',update=update,title=title)

@main.route('/blog/<int:id>',methods=["GET","POST"])
@login_required
def blog(id):
    blog = Blog.get_blog(id)
    comments = Comments.get_comments(blog)
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment = comment_form.comments.data
        new_comment = Comments(comment=comment,review=blog,user=current_user)
        new_comment.save_comment()

        return redirect(url_for('main.blog',id=blog.id))


    return render_template('blog.html',comment_form=comment_form,blog=blog,comments=comments)

@main.route('/reset_password',methods=["GET","POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('.index'))

    request_form = ResetPasswordRequest()
    if request_form.validate_on_submit():
        user = User.query.filter_by(email=request_form.email.data).first()
        send_reset_email(user)

        return redirect(url_for('auth.login'))

    return render_template('reset_request.html',request_form=request_form)

@main.route('/reset_password/<token>',methods=["GET","POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('.index'))
    user = User.verify_token(token)
    if user is None:
        return redirect(url_for('reset_request'))

    reset_form = ResetPassword()
    if reset_form.validate_on_submit():
        new_password = reset_form.new_password.data
        user.password = new_password
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('reset.html',reset_form=reset_form)