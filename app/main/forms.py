from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, ValidationError,
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User, Subscribe

# class ReviewForm(FlaskForm):

#     title = StringField()
#     review = TextAreaField()
#     submit = SubmitField("Submit")


# class UpdateProfile(FlaskForm):
#     bio = TextAreaField()
#     submit = SubmitField("Submit")

class LoginForm(FlaskForm):

    username = StringField("Username:", validators=[Required()])
    password = PasswordField("Password:", validators=[Required()])
    submit = SubmitField("login")


class EditPostForm(FlaskForm):

    title = StringField("", validators=[Required()])
    content = TextAreaField("", validators=[Required()])
    submit = SubmitField("post")


class SignUpForm(FlaskForm):

    name = StringField("Name:", validators=[Required()])
    username = StringField("Username:", validators=[Required()])
    email = StringField("Email:", validators=[Required(),Email()])
    password = PasswordField('Password', validators = [Required(),EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password', validators = [Required()])
    submit  = SubmitField("signup")