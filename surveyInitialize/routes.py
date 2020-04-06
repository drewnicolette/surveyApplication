from flask import render_template, flash, redirect, url_for
from surveyInitialize.models import User, Post
from surveyInitialize import app, db, bcrypt

#From forms file... import registration form and login forms (These are classes that include fields to display on the homescreen along with rules for each field)
from surveyInitialize.forms import RegistrationForm, LoginForm, QuestionForm

#Renders the login.html template in /template directory
@app.route("/", methods=['GET','POST'])
def hello():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash(f"Successful Login for: {form.email.data}!", "success")
            return redirect(url_for('about'))
        else:
            flash(f"Login Unsuccessful. Please try again!","danger")

    return render_template('login.html', title='Login', form=form)

#Looks for about.html template in the /template directory
@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password=hashed_password)
        db.session.add(user) #Adds user to DB
        db.session.commit() #Commits user to DB
        flash(f"Your Account has been created and now able to log in!", "success")
        return redirect(url_for("hello"))
    return render_template('register.html', title='Register', form=form)

@app.route("/questions", methods=['GET','POST'])
def question():
    form = QuestionForm()
    if form.validate_on_submit():
        flash(f"Form Submitted!", "success")
        return redirect(url_for("hello")) #CHANGE THIS BACK TO SURVEY PAGE!!!!
    return render_template('questions.html', title='Questions', form=form)