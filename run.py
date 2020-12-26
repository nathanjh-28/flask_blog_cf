# from datetime import datetime
#__ This imports the module Flask and makes an instance of it called app.




from flaskblog import app


#__ This allows you to not have to set your environment variable every time you open a new terminal to run your server.  You can just type python flaskblog.py to run it.
if __name__ == '__main__':
    app.run(debug=True)

