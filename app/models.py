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

    @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
            return check_password_hash(self.password_hash, password)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    def has_roles(self, *args):
        return set(args).issubset({ role.role_name for role in self.roles}


    def __repr__(self):
        return f'User {self.username}'

    # class PhotoProfile(db.Model):
    #     __tablename__='profile_photos'

    #     id = db.Column(db.Integer,primary_key=True)
    #     pic_path = db.Column(db.String())
    #     user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

class Role(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer,primary_key = True)
    role_name = db.Column(db.String(255))
    # users = db.relationship('User',backref = 'role', lazy = "dynamic")

class UserRoles(db.Model):
    __tablename__ = 'user_roles'   

    id = db.Column(db.Integer, primary_key = True)
    user__id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

user_manager = UserManager(app, db, User)
   
   
    def __repr__(self):
        return f'User {self.name}'
