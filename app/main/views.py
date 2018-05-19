from flask import render_template, request, redirect, url_for,flash,current_app as app, abort
from .import main
from ..models import User, Role, Post, Comment, Subscribe
from .forms import LoginForm, EditPostForm, SignUpForm, SubscribeForm
from flask_login import login_user, current_user, login_required, logout_user
from ..import db, photos
from ..auth import OAuthSignIn
from flask_user import UseerManager, roles_required, roles_accepted
from datetime import datetime
import time
from ..email import mail_message
import markdown2



@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():

    """
    View root page function that returns the index page and
    its data
    """

    subscribe_form = SubscribeForm()

    def date_to_local(utc_datetime):
    	now_timestamp = time.time()
    	offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    	return utc_datetime + offset


    user = User.query.filter_by(username=app.config['ADMIN_USERNAME']).first()
    page =request.args.get('page',1, type=int)
    max_page =app.config['POSTS_PER_PAGE']
    posts = Post.query.order_by(Post.time_updated.desc()).paginate(page, max_page, False)

    next_url = url_for('main.index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html',Comment = Comment,subscribe_form=subscribe_form,date_to_local=date_to_local,user=user, posts = posts.items, next_url = next_url, prev_url = prev_url)


@main.route('/subscribe',methods=['GET','POST'])
def subscribe():
    form = SubscribeForm()
    if form.validate_on_submit():
        user = Subscribe(email = form.email.data)
        db.session.add(user)
        db.session.commit()

        flash("You have been subscribed successfully", "success")
    else:
        flash("No email provided", "warning")

    return redirect(url_for('main.index'))


@main.route('/signup',methods=['GET','POST'])
def register():

    form = SignupForm()
    
    if form.validate_on_submit():
        user = User(name = form.name.data, email = form.email.data, username = form.username.data,password=form.password.data)
        user.roles.append(Role(role_name='User'))
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to tweet some", "email/welcome_user", user.email, user = user)

        return redirect(url_for('main.login'))

    if current_user.is_authenticated:
        return redirect (url_for('main.index'))

    return render_template('register.html',signupform = form)




@main.route('/login',methods=['GET','POST'])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password','danger')

    if current_user.is_authenticated:
        return redirect (url_for('main.index'))

    return render_template('login.html', login_form = login_form)


@main.route('/delete/<post_id>',methods=['GET','POST'])
@login_required
def delete(post_id):
    
    try:
        post = Post.query.filter(Post.id == post_id).delete()
        db.session.commit()
        flash("Post deleted","warning")
    except:
        flash("Post not deleted","danger")
        return redirect(url_for('main.index'))
    return redirect(url_for('main.index'))



@main.route('/deletecomment/<comment_id>',methods=['GET','POST'])
@login_required
def deletecomment(comment_id):
    
    try:
        comment = Comment.query.filter(Comment.id == comment_id).delete()
        db.session.commit()
        flash("Comment deleted","info")
    except:
        flash("Comment not deleted","danger")
        return redirect(url_for('main.index'))
    return redirect(url_for('main.index'))