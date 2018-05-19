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

        flash("You have been subscribed successfully","success")
    else:
        flash("No email provided","warning")

    return redirect(url_for('main.index'))
