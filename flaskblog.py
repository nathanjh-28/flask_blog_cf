#__ This imports the module Flask and makes an instance of it called app.
from flask import Flask
app = Flask(__name__)

#__ Use decorators for paths and functions to handle the response
@app.route("/")
def hello():
    return "<h1> Hello World! </h1>"
