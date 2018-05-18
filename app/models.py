from .import db, login_manager
from flask_login import UserMixin
from flask_user import UserManager
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String())
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    password_hash = db.Column(db.String(255))
    comment_id = db.relationship('Comment', backref='user_post')
    role = db.relationship('Role', secondary=('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # reviews = db.relationship('Review', backref = 'user', lazy = "dynamic")
    # photos = db.relationship('PhotoProfile',backref='user',lazy='dynamic')

