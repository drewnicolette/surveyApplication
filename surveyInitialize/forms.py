from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Frond end fields
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    firstname = StringField('Firstname',validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    submit = SubmitField('Sign up')

#Front end fields
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

#Front end fields
class QuestionForm(FlaskForm):
    answer1 = StringField('Answer1',validators=[DataRequired()])
    answer2 = StringField('Answer2',validators=[DataRequired()])
    answer3 = StringField('Answer3',validators=[DataRequired()])

