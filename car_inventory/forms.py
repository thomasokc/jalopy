from click import confirm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [InputRequired(),Email()])
    password = PasswordField('Password', validators = [InputRequired(),EqualTo("confirm", message = "Make sure that your passwords match.")])
    confirm = PasswordField('Repeat Password')
    submit_button = SubmitField()