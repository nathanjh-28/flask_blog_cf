#__ This imports the module Flask and makes an instance of it called app.
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


#___ not so secret key
app.config['SECRET_KEY'] = 'asjldhfalkjsdhfjashdljfkha'

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




#__ This allows you to not have to set your environment variable every time you open a new terminal to run your server.  You can just type python flaskblog.py to run it.
if __name__ == '__main__':
    app.run(debug=True)

