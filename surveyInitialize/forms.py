from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from surveyInitialize.models import User

#Frond end fields
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    firstname = StringField('Firstname',validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username Already Exists! Please choose again!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email Already Exists! Please choose again!')

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
    submit = SubmitField('Check')


class SurveyForm(FlaskForm):
    submit = SubmitField('submit')

