from flask import render_template, flash, redirect, url_for, request
from surveyInitialize.models import User, Post
from surveyInitialize import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

#From forms file... import registration form and login forms (These are classes that include fields to display on the homescreen along with rules for each field)
from surveyInitialize.forms import RegistrationForm, LoginForm, QuestionForm, SurveyForm

#Renders the login.html template in /template directory
@app.route("/", methods=['GET','POST'])
def hello():
    if current_user.is_authenticated:
        return redirect(url_for('survey'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): #Checks if user exists and password is equal to hashed password in db and unhashed password
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next') #Gets page that they wanted to go to
            return redirect(next_page) if next_page else redirect(url_for('survey')) #if next_page is none redirect to question, else redirect to page wanted to access
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
        flash(f"Your Account has been created and you are now able to log in!", "success")
        return redirect(url_for("hello"))
    return render_template('register.html', title='Register', form=form)

@app.route("/questions", methods=['GET','POST'])
@login_required
def question():
    form = QuestionForm()
    if form.validate_on_submit():
        flash(f"Form Submitted!", "success")
        return redirect(url_for("survey")) #CHANGE THIS BACK TO SURVEY PAGE!!!!
    return render_template('questions.html', title='Questions', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('hello'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route("/survey", methods=['GET','POST'])
@login_required
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        flash(f"Survey Submitted", "success")
        return redirect(url_for('question'))
    return render_template('survey.html', title='Survey', form=form)