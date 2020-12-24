#__ This imports the module Flask and makes an instance of it called app.
from flask import Flask
app = Flask(__name__)

#__ Use decorators for paths and functions to handle the response
@app.route("/")
@app.route("/home")
def hello():
    return "<h1> Hello World! </h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

#__ This allows you to not have to set your environment variable every time you open a new terminal to run your server.  You can just type python flaskblog.py to run it.
if __name__ == '__main__':
    app.run(debug=True)

