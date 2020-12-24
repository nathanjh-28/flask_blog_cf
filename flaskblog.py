#__ This imports the module Flask and makes an instance of it called app.
from flask import Flask, render_template, url_for
app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

#__ This allows you to not have to set your environment variable every time you open a new terminal to run your server.  You can just type python flaskblog.py to run it.
if __name__ == '__main__':
    app.run(debug=True)

