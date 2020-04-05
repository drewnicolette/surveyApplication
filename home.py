from flask import Flask, render_template, flash, redirect, url_for
app = Flask(__name__) #Knows where to look for template and static files

#From forms file... import registration form and login forms (These are classes that include fields to display on the homescreen along with rules for each field)
from forms import RegistrationForm, LoginForm

#To get started - Run: export FLASK_APP=frontEnd.py
#To move to debug mode - Run: export FLASK_DEBUG=1
#To start web server - flask run

#Set secret key
app.config['SECRET_KEY'] = '123456789'


#Looks for home.html template in /template directory
@app.route("/")
def hello():
    form = LoginForm()
    return render_template('login.html', form=form)

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

#Keeps it in Debug mode
if __name__ == '__main__':
    app.run(debug=True)