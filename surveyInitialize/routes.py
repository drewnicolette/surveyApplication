from flask import render_template, flash, redirect, url_for
from surveyInitialize.db import User, Post
from surveyInitialize import app

#From forms file... import registration form and login forms (These are classes that include fields to display on the homescreen along with rules for each field)
from surveyInitialize.forms import RegistrationForm, LoginForm

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
        flash(f"Account Created for {form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash(f"Successful Login for: {form.email.data}!", "success")
            return redirect(url_for('about'))
        else:
            flash(f"Login Unsuccessful. Please try again!","danger")

    return render_template('login.html', title='Login', form=form)