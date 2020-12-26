from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
#___ Models
from flaskblog.models import User, Post



#__ "dummy" data
posts = [
    {
        'author': 'Nathan Harris',
        'title': 'Blog Post 1',
        'content': 'Lorem Ipsum blah blah blah',
        'date_posted': 'April 20, 2018'
    },
        {
        'author': 'Jeff Smitty',
        'title': 'Blog Post 2',
        'content': 'hello world my name is Jeffff and I like to party!',
        'date_posted': 'May 1, 2018'
    }
]


#__ Use decorators for paths and functions to handle the response
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for(home))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
        # if form.email.data == 'me@example.com' and etc
    # else:
        # flash('login uncucessful', 'danger')
    return render_template('login.html', title='Login', form=form)