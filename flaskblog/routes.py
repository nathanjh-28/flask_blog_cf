from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required



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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created!  You are able to login','success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next') 
            return redirect(nextpage) if next_page else redirect(url_for('home'))
        else:
            flash('login uncucessful.  Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')