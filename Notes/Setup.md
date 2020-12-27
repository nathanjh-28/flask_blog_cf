boilerplate checklist:
install dependencies (make a list)
files and folder structure
database connection and other needed variables
set up template inheritence and link up stylesheet
basic routes
user model and auth
<br>
# Flask Setup

Getting Files and Folders Setup
1\. Make project directory and `cd` in to it.  Create virtual environment and enter it.

`python3 -m venv .env`
`source .env/bin/activate`

2\. Install Flask
`% pip install Flask`
3\. Create your entry point python file\, it could be index\.py or server\.py or app\.py\, for this tutorial we are using flaskblog\.py
`% touch flaskblog.py`

**/app.py**

<span class="colour" style="color:rgb(106, 153, 85)">#\_\_ This imports the module Flask and makes an instance of it called app.</span>
<span class="colour" style="color:rgb(86, 156, 214)">from</span><span class="colour" style="color:rgb(212, 212, 212)"> flask </span><span class="colour" style="color:rgb(86, 156, 214)">import</span><span class="colour" style="color:rgb(212, 212, 212)"> Flask</span>
<span class="colour" style="color:rgb(212, 212, 212)">app = Flask(\_\_name\_\_)</span>

<span class="colour" style="color:rgb(106, 153, 85)">#\_\_ Use decorators for paths and functions to handle the response</span>
<span class="colour" style="color:rgb(212, 212, 212)">@app.route(</span><span class="colour" style="color:rgb(206, 145, 120)">"/"</span><span class="colour" style="color:rgb(212, 212, 212)">) </span>
<span class="colour" style="color:rgb(86, 156, 214)">def</span><span class="colour" style="color:rgb(212, 212, 212)"> hello():</span>
<span class="colour" style="color:rgb(86, 156, 214)">return</span><span class="colour" style="color:rgb(212, 212, 212)"> </span><span class="colour" style="color:rgb(206, 145, 120)">"Hello World!"</span>

4\. Set environment variable in terminal\.  This sets the entry point for the server\.
`% export FLASK_APP=flaskblog.py`
Run the server
`% flask run`

5\. Debug Mode
`% export FLASK_DEBUG=1`
This allows your server to refresh on it's own so you don't have to restart your server every time.

6\. Setting the environment variable long term\, this is a python way of doing this not necessarily Flask\.  \(brush up on name=main topic\)
<span class="colour" style="color:rgb(106, 153, 85)">#\_\_ This allows you to not have to set your environment variable every time you open a new terminal to run your server. You can just type `python flaskblog.py` to run it.</span>
<span class="colour" style="color:rgb(86, 156, 214)">if</span><span class="colour" style="color:rgb(212, 212, 212)"> \_\_name\_\_ == </span><span class="colour" style="color:rgb(206, 145, 120)">'\_\_main\_\_'</span><span class="colour" style="color:rgb(212, 212, 212)">:</span>
<span class="colour" style="color:rgb(212, 212, 212)">app.run(debug=</span><span class="colour" style="color:rgb(86, 156, 214)">True</span><span class="colour" style="color:rgb(212, 212, 212)">)</span>

7.  With the previous way, setting up the environment variable with set... you can run flask in terminal (app instance and database already connected) as well as flask run when wanting to run the server.
`% flask run // run server`
`% flask shell // run flask terminal`

8\. Decorators and Routes
You can use multiple decorators / url paths for one view function.
<span class="colour" style="color:rgb(212, 212, 212)">@app.route(</span><span class="colour" style="color:rgb(206, 145, 120)">"/"</span><span class="colour" style="color:rgb(212, 212, 212)">)</span>
<span class="colour" style="color:rgb(212, 212, 212)">@app.route(</span><span class="colour" style="color:rgb(206, 145, 120)">"/home"</span><span class="colour" style="color:rgb(212, 212, 212)">)</span>
<span class="colour" style="color:rgb(86, 156, 214)">def</span><span class="colour" style="color:rgb(212, 212, 212)"> hello():</span>
<span class="colour" style="color:rgb(86, 156, 214)">return</span><span class="colour" style="color:rgb(212, 212, 212)"> </span><span class="colour" style="color:rgb(206, 145, 120)">"\<h1> Hello World! \</h1>"</span>

# Templates

Previously we were return HTML as a string.  Now we will render an html template
1.  Create Templates Directory, call it "templates"
2.  Make some templates!  home.html and about.html
Add some boilerplate and put a heading in to test it.
3.  Back in our flaskblog.py file we need to import the render\_template function from flask.
<span class="colour" style="color:rgb(86, 156, 214)">from</span><span class="colour" style="color:rgb(212, 212, 212)"> flask </span><span class="colour" style="color:rgb(86, 156, 214)">import</span><span class="colour" style="color:rgb(212, 212, 212)"> Flask, render\_template</span>
And now we can return the function of render\_template with the argument of the name of the html file.
<span class="colour" style="color:rgb(86, 156, 214)">return</span><span class="colour" style="color:rgb(212, 212, 212)"> render\_template(</span><span class="colour" style="color:rgb(206, 145, 120)">'home.html'</span><span class="colour" style="color:rgb(212, 212, 212)">)</span>
4\. Showing data in Templates\.\.\. We can get started by writng some "dummy data" in our flaskblog\.py file\.
<span class="colour" style="color:rgb(106, 153, 85)">#\_\_ "dummy" data</span>
<span class="colour" style="color:rgb(212, 212, 212)">posts = [</span>
<span class="colour" style="color:rgb(212, 212, 212)">{</span>
<span class="colour" style="color:rgb(206, 145, 120)">'author'</span><span class="colour" style="color:rgb(212, 212, 212)">: </span><span class="colour" style="color:rgb(206, 145, 120)">'Nathan Harris'</span><span class="colour" style="color:rgb(212, 212, 212)">,</span>
<span class="colour" style="color:rgb(206, 145, 120)">'title'</span><span class="colour" style="color:rgb(212, 212, 212)">: </span><span class="colour" style="color:rgb(206, 145, 120)">'Blog Post 1'</span><span class="colour" style="color:rgb(212, 212, 212)">,</span>
<span class="colour" style="color:rgb(206, 145, 120)">'content'</span><span class="colour" style="color:rgb(212, 212, 212)">: </span><span class="colour" style="color:rgb(206, 145, 120)">'Lorem Ipsum blah blah blah'</span><span class="colour" style="color:rgb(212, 212, 212)">,</span>
<span class="colour" style="color:rgb(206, 145, 120)">'date\_posted'</span><span class="colour" style="color:rgb(212, 212, 212)">: </span><span class="colour" style="color:rgb(206, 145, 120)">'April 20, 2018'</span>
<span class="colour" style="color:rgb(212, 212, 212)">},</span>
<span class="colour" style="color:rgb(212, 212, 212)">{</span>
<span class="colour" style="color:rgb(206, 145, 120)">'author'</span><span class="colour" style="color:rgb(212, 212, 212)">: </span><span class="colour" style="color:rgb(206, 145, 120)">'Jeff Smitty'</span><span class="colour" style="color:rgb(212, 212, 212)">,</span>
<span class="colour" style="color:rgb(206, 145, 120)">'title'</span><span class="colour" style="color:rgb(212, 212, 212)">: </span><span class="colour" style="color:rgb(206, 145, 120)">'Blog Post 2'</span><span class="colour" style="color:rgb(212, 212, 212)">,</span>
<span class="colour" style="color:rgb(206, 145, 120)">'content'</span><span class="colour" style="color:rgb(212, 212, 212)">: </span><span class="colour" style="color:rgb(206, 145, 120)">'hello world my name is Jeffff and I like to party!'</span><span class="colour" style="color:rgb(212, 212, 212)">,</span>
<span class="colour" style="color:rgb(206, 145, 120)">'date\_posted'</span><span class="colour" style="color:rgb(212, 212, 212)">: </span><span class="colour" style="color:rgb(206, 145, 120)">'May 1, 2018'</span>
<span class="colour" style="color:rgb(212, 212, 212)">}</span>
<span class="colour" style="color:rgb(212, 212, 212)">]</span>

To pass this data in to our template we add a second argument to the render\_template function and write a kwarg... posts=posts.  the first posts refers to the data in the template and the second refers to the data in this file.

5.  We can use Jinja2 logic in our html template files to loop through data or use conditionals to hide and show data.
{% logic goes in between these tags %}
{{ content goes in between these tags }}
To write a for loop (and other things) you have to make an ending tag for it.  {% endfor %}

<span class="colour" style="color:rgb(212, 212, 212)">{% </span><span class="colour" style="color:rgb(86, 156, 214)">for</span><span class="colour" style="color:rgb(212, 212, 212)"> post </span><span class="colour" style="color:rgb(86, 156, 214)">in</span><span class="colour" style="color:rgb(212, 212, 212)"> posts %}</span>
<span class="colour" style="color:rgb(128, 128, 128)"><</span><span class="colour" style="color:rgb(86, 156, 214)">h3</span><span class="colour" style="color:rgb(128, 128, 128)">></span><span class="colour" style="color:rgb(212, 212, 212)">{{ post.title }}</span><span class="colour" style="color:rgb(128, 128, 128)"></</span><span class="colour" style="color:rgb(86, 156, 214)">h3</span><span class="colour" style="color:rgb(128, 128, 128)">></span>
<span class="colour" style="color:rgb(128, 128, 128)"><</span><span class="colour" style="color:rgb(86, 156, 214)">h4</span><span class="colour" style="color:rgb(128, 128, 128)">></span><span class="colour" style="color:rgb(212, 212, 212)">By {{ post.author }} on {{ post.date\_posted }}</span><span class="colour" style="color:rgb(128, 128, 128)"></</span><span class="colour" style="color:rgb(86, 156, 214)">h4</span><span class="colour" style="color:rgb(128, 128, 128)">></span>
<span class="colour" style="color:rgb(128, 128, 128)"><</span><span class="colour" style="color:rgb(86, 156, 214)">p</span><span class="colour" style="color:rgb(128, 128, 128)">></span><span class="colour" style="color:rgb(212, 212, 212)">{{ post.content }}</span><span class="colour" style="color:rgb(128, 128, 128)"></</span><span class="colour" style="color:rgb(86, 156, 214)">p</span><span class="colour" style="color:rgb(128, 128, 128)">></span>
<span class="colour" style="color:rgb(212, 212, 212)">{% </span><span class="colour" style="color:rgb(86, 156, 214)">endfor</span><span class="colour" style="color:rgb(212, 212, 212)"> %}</span>

6.  Conditionals are written like this:  {% if something%} do this {% else %} other things {% endif %}.  Don't forget the endif otherwise you get an error.

<span class="colour" style="color:rgb(212, 212, 212)">{% </span><span class="colour" style="color:rgb(86, 156, 214)">if</span><span class="colour" style="color:rgb(212, 212, 212)"> title %}</span>
<span class="colour" style="color:rgb(128, 128, 128)"><</span><span class="colour" style="color:rgb(86, 156, 214)">title</span><span class="colour" style="color:rgb(128, 128, 128)">></span><span class="colour" style="color:rgb(212, 212, 212)">Flask Blog - {{ title }}</span><span class="colour" style="color:rgb(128, 128, 128)"></</span><span class="colour" style="color:rgb(86, 156, 214)">title</span><span class="colour" style="color:rgb(128, 128, 128)">></span>
<span class="colour" style="color:rgb(212, 212, 212)">{% </span><span class="colour" style="color:rgb(86, 156, 214)">else</span><span class="colour" style="color:rgb(212, 212, 212)"> %}</span>
<span class="colour" style="color:rgb(128, 128, 128)"><</span><span class="colour" style="color:rgb(86, 156, 214)">title</span><span class="colour" style="color:rgb(128, 128, 128)">></span><span class="colour" style="color:rgb(212, 212, 212)">Flask Blog</span><span class="colour" style="color:rgb(128, 128, 128)"></</span><span class="colour" style="color:rgb(86, 156, 214)">title</span><span class="colour" style="color:rgb(128, 128, 128)">></span>
<span class="colour" style="color:rgb(212, 212, 212)">{% </span><span class="colour" style="color:rgb(86, 156, 214)">endif</span><span class="colour" style="color:rgb(212, 212, 212)"> %}</span>

If we add the kwarg of title to the render\_template function we can append the title of the document.
<br>
### 7.  Template Inheritence
<br>
To avoid writing html over and over we can write child snippets and have parent templates inherit them.

Create an html file, in this tutorial we call it layout.html

You can type your html boilerplate and then in the body write
{% block content %}
This will indicate where you want the child snippet to overwrite
Here we are calling the block "content"
Need to close it with an {% endblock %}

Now we go to our child html snippet and delete the boilerplate leaving just the content that we want to override in the parent html file.

We start by writing {% extends "layout.html" %} at the top

Wrap your snippet with {% block content %} and {% endblock %}
Optionally you can add content to endblock to help you remember what block you are ending.  {% endblock content %}

You can also import an html partial by using the includes keyword (Miguel Grinberg's blog)

8.  Styling and CSS

He adds the link to bootstrap in his layout.html so that he can use bootstrap across all templates.

Create a folder called "static" and place your front end CSS and JS files there.  Import the url\_for function from flask to your flaskblog.py

<span class="colour" style="color:rgb(86, 156, 214)">from</span><span class="colour" style="color:rgb(212, 212, 212)"> flask </span><span class="colour" style="color:rgb(86, 156, 214)">import</span><span class="colour" style="color:rgb(212, 212, 212)"> Flask, render\_template, url\_for</span>

url\_for allows you to pass variables and convert them to url or file paths

Basically all the front end styling is done at this point.
<br>
# Forms and Validation
<br>
Popular forms tool for Flask is WTForms.

`% pip install flask-wtf`

Create a file called forms.py so that we can keep our forms in one place and separate from our entry server file.

This tool allows us to write python classes and then they are converted to html forms.  We need to install quite a few dependencies to make our forms.

/forms.py
<span class="colour" style="color:rgb(106, 153, 85)">`#___ Import Module`</span>

<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">` flask_wtf `</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` FlaskForm`</span>
<span class="colour" style="color:rgb(106, 153, 85)">`#___ Form Fields`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">` wtforms `</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` StringField, PasswordField, SubmitField, BooleanField`</span>
<span class="colour" style="color:rgb(106, 153, 85)">`#___ Validators`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">` wtforms.validators `</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` DataRequired, Length, Email, EqualTo`</span>

When writing your input you select a field, you give it a name for the class and then the first argument is a string that will be the label for that input.  Next you can add your validators in an array, make sure you invoke them.  DataRequired means they can't leave it blank, Length takes two kwargs min and max, Email checks for valid email address, and EqualTo allows you to compare the two password fields and make sure they match.

Registration Form:

<span class="colour" style="color:rgb(86, 156, 214)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">` RegistrationForm(FlaskForm):`</span>

<span class="colour" style="color:rgb(212, 212, 212)">`username = StringField(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Username'`</span><span class="colour" style="color:rgb(212, 212, 212)">`,`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`validators=[`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`DataRequired(),`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`Length(min=`</span><span class="colour" style="color:rgb(181, 206, 168)">`2`</span><span class="colour" style="color:rgb(212, 212, 212)">`, max=`</span><span class="colour" style="color:rgb(181, 206, 168)">`20`</span><span class="colour" style="color:rgb(212, 212, 212)">`)]),`</span>

<span class="colour" style="color:rgb(212, 212, 212)">`email = StringField(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Email'`</span><span class="colour" style="color:rgb(212, 212, 212)">`,`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`validators=[`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`DataRequired(),`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`Email()]),`</span>

<span class="colour" style="color:rgb(212, 212, 212)">`password = PasswordField(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Password'`</span><span class="colour" style="color:rgb(212, 212, 212)">`,`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`validators=`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`DataRequired()),`</span>

<span class="colour" style="color:rgb(212, 212, 212)">`confirm_password = PasswordField(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Confirm Password'`</span><span class="colour" style="color:rgb(212, 212, 212)">`,`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`validators=[`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`DataRequired(),`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`EqualTo(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'password'`</span><span class="colour" style="color:rgb(212, 212, 212)">`)])`</span>

<span class="colour" style="color:rgb(212, 212, 212)">`submit = SubmitField(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Sign Up'`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>

2\. Secret Key

Add a secret key to your flaskblog.py file

<span class="colour" style="color:rgb(212, 212, 212)">`app.config[`</span><span class="colour" style="color:rgb(206, 145, 120)">`'SECRET_KEY'`</span><span class="colour" style="color:rgb(212, 212, 212)">` = `</span><span class="colour" style="color:rgb(206, 145, 120)">`' < top secret key goes here > '`</span><span class="colour" style="color:rgb(212, 212, 212)">`]`</span>

3.  Import forms in to flaskblog.py

/flaskblog.py
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">` forms `</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` RegistrationForm, LoginForm`</span>

<br>
4.  Add routes for login and registration

We want to create instances of the forms set to variable form and pass them in to the template upon rendering.

<span class="colour" style="color:rgb(212, 212, 212)">`@app.route(`</span><span class="colour" style="color:rgb(206, 145, 120)">`"/register"`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>

<span class="colour" style="color:rgb(86, 156, 214)">`def`</span><span class="colour" style="color:rgb(212, 212, 212)">` register():`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`form = RegistrationForm()`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`return`</span><span class="colour" style="color:rgb(212, 212, 212)">` render_template(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'register.html'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, title=`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Register'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, form=form)`</span>

<span class="colour" style="color:rgb(212, 212, 212)">`@app.route(`</span><span class="colour" style="color:rgb(206, 145, 120)">`"/login"`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`def`</span><span class="colour" style="color:rgb(212, 212, 212)">` login():`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`form = LoginForm()`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`return`</span><span class="colour" style="color:rgb(212, 212, 212)">` render_template(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'login.html'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, title=`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Login'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, form=form)`</span>

5.  Make Login and Register Templates

Bring in the extends keyword to layout.html as well as block content and endblock
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`extends`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(206, 145, 120)">`"layout.html"`</span><span class="colour" style="color:rgb(212, 212, 212)">` %}`</span>

<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`block`</span><span class="colour" style="color:rgb(212, 212, 212)">` content %}`</span>
<span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`h1`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span><span class="colour" style="color:rgb(212, 212, 212)">`Login`</span><span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`h1`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`endblock`</span><span class="colour" style="color:rgb(212, 212, 212)">` content %}`</span>

Now to access the form that we are passing in to the template we just start with form.username or whatever is the field name on the class.  You can also pass in CSS classes as kwargs.  You can make an html element for the label using the label in the class and an element for the input field.

Start your form with your CSRF token

<span class="colour" style="color:rgb(212, 212, 212)">`{{ form.hidden_tag() }}`</span>

Label - <span class="colour" style="color:rgb(212, 212, 212)">`{{ form.username.label(class=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"classes-go-here"`</span><span class="colour" style="color:rgb(212, 212, 212)">`) }}`</span>

<span class="colour" style="color:rgb(212, 212, 212)">Field - `{{ form.username(class=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"classes-go-here"`</span><span class="colour" style="color:rgb(212, 212, 212)">`) }}`</span>

6.  POST requests...

We need to modify the app.route decorator for the destination of our form submission otherwise we get an error that you cannot POST to that URL.

<span class="colour" style="color:rgb(212, 212, 212)">`@app.route(`</span><span class="colour" style="color:rgb(206, 145, 120)">`"/register"`</span><span class="colour" style="color:rgb(212, 212, 212)">`, methods=[`</span><span class="colour" style="color:rgb(206, 145, 120)">`'GET'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, `</span><span class="colour" style="color:rgb(206, 145, 120)">`'POST'`</span><span class="colour" style="color:rgb(212, 212, 212)">`])`</span>

<br>
7.  Form Validation

In our POST route we can validate the incoming form and for now we pass a flash message to confirm post.
<span class="colour" style="color:rgb(86, 156, 214)">`if`</span><span class="colour" style="color:rgb(212, 212, 212)">` form.validate_on_submit():`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`flash(`</span><span class="colour" style="color:rgb(86, 156, 214)">`f`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Account created for `</span><span class="colour" style="color:rgb(212, 212, 212)">`{form.username.data}`</span><span class="colour" style="color:rgb(206, 145, 120)">`!'`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>

<span class="colour" style="color:rgb(212, 212, 212)">make sure to import flash</span>
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flask`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` Flask, render_template, url_for, flash`</span>

Now if we want to see these messages in the browser we have to put some html in to our layout template.  We can also pass in a class by using the category argument in the flash function
<span class="colour" style="color:rgb(212, 212, 212)">`flash(`</span><span class="colour" style="color:rgb(86, 156, 214)">`f`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Account created for `</span><span class="colour" style="color:rgb(212, 212, 212)">`{form.username.data}`</span><span class="colour" style="color:rgb(206, 145, 120)">`!', 'success'`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>

So here we are passing the word success in as the message category and we can then use that as a class to style the message.  So success could be gree/blue and invalid can be red or whatever.

<br>
/layout.html
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`with`</span><span class="colour" style="color:rgb(212, 212, 212)">` messages = get_flashed_messages(with_categories=`</span><span class="colour" style="color:rgb(86, 156, 214)">`true`</span><span class="colour" style="color:rgb(212, 212, 212)">`) %}`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`if`</span><span class="colour" style="color:rgb(212, 212, 212)">` messages %}`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`for`</span><span class="colour" style="color:rgb(212, 212, 212)">`category, message`</span><span class="colour" style="color:rgb(86, 156, 214)">`in`</span><span class="colour" style="color:rgb(212, 212, 212)">` messages %}`</span>
<span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`div`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"alert alert-{{ category }}"`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{{ message }}`</span>
<span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`div`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`endfor`</span><span class="colour" style="color:rgb(212, 212, 212)">` %}`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`endif`</span><span class="colour" style="color:rgb(212, 212, 212)">` %}`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`endwith`</span><span class="colour" style="color:rgb(212, 212, 212)">` %}`</span>

8\. User Validation in the HTML form

It would be better if the user got feedback while filling out the form instead of waiting for submit.  Also, it takes some of the weight off of our server and utilizes their browser.

One Example in /register.html
<span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`div`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"form-group"`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{{ form.username.label(class=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"form-control-label"`</span><span class="colour" style="color:rgb(212, 212, 212)">`) }}`</span>

<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`if`</span><span class="colour" style="color:rgb(212, 212, 212)">` form.username.errors %}`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{{ form.username(class=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"form-control form-control-lg is-invalid"`</span><span class="colour" style="color:rgb(212, 212, 212)">`) }}`</span>
<span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`div`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"invalid-feedback"`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`for`</span><span class="colour" style="color:rgb(212, 212, 212)">`error`</span><span class="colour" style="color:rgb(86, 156, 214)">`in`</span><span class="colour" style="color:rgb(212, 212, 212)">` form.username.errors %}`</span>
<span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`span`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span><span class="colour" style="color:rgb(212, 212, 212)">`{{ error }}`</span><span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`span`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`endfor`</span><span class="colour" style="color:rgb(212, 212, 212)">` %}`</span>
<span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`div`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`else`</span><span class="colour" style="color:rgb(212, 212, 212)">` %}`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{{ form.username(class=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"form-control form-control-lg"`</span><span class="colour" style="color:rgb(212, 212, 212)">`) }}`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`endif`</span><span class="colour" style="color:rgb(212, 212, 212)">` %}`</span>
<span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`div`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>

For login we copy and paste and modify.  The route for login will have to wait until database is up and running.
For the sake of an example to test we put in a hardcoded user info to test the validation messages.

9.  Nav Bar clean up, we can use url\_for() to pass routes in to links in our nav bar.
<span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`a `</span><span class="colour" style="color:rgb(156, 220, 254)">`href`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"{{ url_for('about') }}"`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span><span class="colour" style="color:rgb(212, 212, 212)">`About`</span><span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`a`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<br>
# Database with Flask-SQL-Alchemy

1.  Setup
SQL Alchemy is an ORM, object relational mapper.  Makes it much easier to work with SQL.  Just like Mongoose for MongoDB.

Install flask sql alchemy

`% pip install flask-sqlalchemy`

Import it in to your project file

/flaskblog.py

<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flask_sqlalchemy`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` SQLAlchemy`</span>

For Development purposes we will use a SQLite file locally and tell the app to look for the Database using the database URI config variable.

/flaskblog.py
<span class="colour" style="color:rgb(212, 212, 212)">`app.config[`</span><span class="colour" style="color:rgb(206, 145, 120)">`'SQLALCHEMY_DATABASE_URI'`</span><span class="colour" style="color:rgb(212, 212, 212)">`] = `</span><span class="colour" style="color:rgb(206, 145, 120)">`'sqlite:///site.db'`</span>

and we need an instance of our database which we will call 'db'

<span class="colour" style="color:rgb(212, 212, 212)">`db = SQLAlchemy(app)`</span>

2.  Models
Now in SQL we have tabels and using this ORM we can make python classes in to those tables for which we call them "Models"

These classes inherit the Model class from our db instance.  `class User(db.Model):`
We use the method of column to indicate a column on the SQL table and then the first argument is the type of data in the column.  db.Integer or db.String etc.  Next we can add whatever kwargs we want for this column

Interestingly, we can set a relationship field for a class to indicate that it has a one to many relationship to another table.  In SQL you only indicate the relationship from the 'many' table by using the foreign key of the 'one' table.  We aren't doing anything different using SQL but we are creating a behind the scenes query with our relationship field on the User class.  Which is why it is called "db.relationship" and we call it "author" when looking it up.

\_\_repr\_\_ method is similar to \_\_str\_\_ method but the idea is that the repr method is for development and the str method is more for the end user.

<span class="colour" style="color:rgb(86, 156, 214)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">` User(db.Model):`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`id = db.Column(db.Integer, primary_key=`</span><span class="colour" style="color:rgb(86, 156, 214)">`True`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`username = db.Column(db.String(`</span><span class="colour" style="color:rgb(181, 206, 168)">`20`</span><span class="colour" style="color:rgb(212, 212, 212)">`), unique=`</span><span class="colour" style="color:rgb(86, 156, 214)">`True`</span><span class="colour" style="color:rgb(212, 212, 212)">`, nullable=`</span><span class="colour" style="color:rgb(86, 156, 214)">`False`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`email = db.Column(db.String(`</span><span class="colour" style="color:rgb(181, 206, 168)">`120`</span><span class="colour" style="color:rgb(212, 212, 212)">`), unique=`</span><span class="colour" style="color:rgb(86, 156, 214)">`True`</span><span class="colour" style="color:rgb(212, 212, 212)">`, nullable=`</span><span class="colour" style="color:rgb(86, 156, 214)">`False`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`image_file = db.Column(db.String(`</span><span class="colour" style="color:rgb(181, 206, 168)">`20`</span><span class="colour" style="color:rgb(212, 212, 212)">`), nullable=`</span><span class="colour" style="color:rgb(86, 156, 214)">`False`</span><span class="colour" style="color:rgb(212, 212, 212)">`, default=`</span><span class="colour" style="color:rgb(206, 145, 120)">`'default.jpg'`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`password = db.Column(db.String(`</span><span class="colour" style="color:rgb(181, 206, 168)">`60`</span><span class="colour" style="color:rgb(212, 212, 212)">`), nullable=`</span><span class="colour" style="color:rgb(86, 156, 214)">`False`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(106, 153, 85)">`#___ Relationship to posts`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`posts = db.relationship(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Post'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, backref=`</span><span class="colour" style="color:rgb(206, 145, 120)">`'author'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, lazy=`</span><span class="colour" style="color:rgb(86, 156, 214)">`True`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>

<span class="colour" style="color:rgb(86, 156, 214)">`def`</span><span class="colour" style="color:rgb(212, 212, 212)">` __repr__(self):`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`return`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(86, 156, 214)">`f`</span><span class="colour" style="color:rgb(206, 145, 120)">`"User('`</span><span class="colour" style="color:rgb(212, 212, 212)">`{ `</span><span class="colour" style="color:rgb(86, 156, 214)">`self`</span><span class="colour" style="color:rgb(212, 212, 212)">`.username }`</span><span class="colour" style="color:rgb(206, 145, 120)">`','`</span><span class="colour" style="color:rgb(212, 212, 212)">`{ `</span><span class="colour" style="color:rgb(86, 156, 214)">`self`</span><span class="colour" style="color:rgb(212, 212, 212)">`.email }`</span><span class="colour" style="color:rgb(206, 145, 120)">`', '`</span><span class="colour" style="color:rgb(212, 212, 212)">`{ `</span><span class="colour" style="color:rgb(86, 156, 214)">`self`</span><span class="colour" style="color:rgb(212, 212, 212)">`.image_file }`</span><span class="colour" style="color:rgb(206, 145, 120)">`' )"`</span>

<span class="colour" style="color:rgb(86, 156, 214)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">` Post(db.Model):`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`id = db.Column(db.Integer, primary_key=`</span><span class="colour" style="color:rgb(86, 156, 214)">`True`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`title = db.Column(db.String(`</span><span class="colour" style="color:rgb(181, 206, 168)">`100`</span><span class="colour" style="color:rgb(212, 212, 212)">`), nullable=`</span><span class="colour" style="color:rgb(86, 156, 214)">`False`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`date_posted = db.Column(db.DateTime, nullable=`</span><span class="colour" style="color:rgb(86, 156, 214)">`False`</span><span class="colour" style="color:rgb(212, 212, 212)">`, default=datetime.utcnow)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`content = db.Column(db.Text, nullable=`</span><span class="colour" style="color:rgb(86, 156, 214)">`False`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`user_id = db.Column(db.Integer, db.ForeignKey(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'user.id'`</span><span class="colour" style="color:rgb(212, 212, 212)">`), nullable=`</span><span class="colour" style="color:rgb(86, 156, 214)">`False`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>

<span class="colour" style="color:rgb(86, 156, 214)">`def`</span><span class="colour" style="color:rgb(212, 212, 212)">` __repr__(self):`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`return`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(86, 156, 214)">`f`</span><span class="colour" style="color:rgb(206, 145, 120)">`"Post('`</span><span class="colour" style="color:rgb(212, 212, 212)">`{ `</span><span class="colour" style="color:rgb(86, 156, 214)">`self`</span><span class="colour" style="color:rgb(212, 212, 212)">`.title }`</span><span class="colour" style="color:rgb(206, 145, 120)">`','`</span><span class="colour" style="color:rgb(212, 212, 212)">`{ `</span><span class="colour" style="color:rgb(86, 156, 214)">`self`</span><span class="colour" style="color:rgb(212, 212, 212)">`.date_posted }`</span><span class="colour" style="color:rgb(206, 145, 120)">`')"`</span>

3.  Database Actions

In the flask shell we can create an instance based on our models.

We can create a database where it will make tables based on our models with

`db.create_all()`

`user_1 = User(username="johndoe", email="`[`myemail@example.com`](mailto:myemail@example.com)`", password="password")`
Now we have a variable with an instance stored called user\_1
We can add it to a staging area in the database
`db.session.add(user_1)`
We can add more here or modify and when we are done we can commit the changes
`db.session.commit()`

Once we have more data in the database we can use these commands and also store lists or individual items in variables.

`User.query.all()` // --> Grabs all users
`User.query.first()` //--> Grabs the first user
`User.query.filter_by(username='johnDoe').all() ` // --> Grabs all users with that username and puts them in a list
`User.query.filter_by(username="johnDoe".first()` // --> Grabs only the fist user with that username and does not put it in a list
`User.query.get(1)` --> Grabs a user by the id of 1

Once we have posts we can use similar queries to grab them but with the relationship field from our user model we can also grab them from a user instance.
`user = User.query.get(1)`
`user.posts` //--> This will show us all the posts that this user has
`post = Post.query.first()`
`post.user_id` // --> This shows the user id of the author of the post
`post.author` // --> Grabs the entire user object associated with this post

We can delete the whole database by using
`db.drop_all()`
To start with a clean slate we can do
`db.create_all()`
and now we have all the tables but no info.

# Package Structuring

So far we have been running our server with out it being in a package.  There are pros and cons to this but as we scale the app we will need to be in a package.  I'm a little confused by the explanation but here is the solution.  I want to reorder this outline so that this part is at the beginning so we can have more of a blank canvas to make our app.  Also the dependency installations in that chapter too.

Old Tree:
/static
    main.css
/templates
    \<templates here>
flaskblog.py
forms.py
site.db

New Tree:
/flaskblog
    \_\_init\_\_.py
    forms.py
    models.py
    routes.py
    site.db
    /static
        main.css
    /templates
        about.html
        home.html
        layout.html
        login.html
        register.html
   run.py

So we have moved our models in to a models.py file and our routes in to a routes.py, some of our logic has now gone in to the init.py and the run.py file.  Obviously we need to revise all of our import statements.

Let's look at run.py and /flaskblog/\_\_init\_\_.py

/run.py
from flaskblog import app
if \_\_name\_\_ == '\_\_main\_\_':
    app.run(debug=True)

/\_\_init\_\_.py
from flask import Flask
from flask\_sqlalchemy import SQLAlchemy

app = Flask(\_\_name\_\_)
app.config['SECRET\_KEY'] = 'secret string of chracters'
app.config['SQLALCHEMY\_DATABASE\_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes

So the run file just initiates the process by running our Flask instance called App.

Init sets up all the config variables we need, sets up our db connection with variable db.

Dependencies in Routes... As you can see in the init file we dumped our routes in to another file.

/routes.py
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flask`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` render_template, url_for, flash, redirect`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flaskblog`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` app`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flaskblog.forms`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` RegistrationForm, LoginForm`</span>
<span class="colour" style="color:rgb(106, 153, 85)">`#___ Models`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flaskblog.models`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` User, Post`</span>

and we have dependencies in models.py

/models.py
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flaskblog`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` db`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`datetime`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` datetime`</span>

If we delete site.db and re establish the database it will be created in our project folder instead of the main directory because it is created in the same folder as the config variables.

<br>
# User Auth
<br>
We need to hash our passwords, lets install bcrypt

`% pip install flask-bcrypt`

flask shell...
from flask\_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.generate\_password\_hash('testing') --> hashed password with a b in front of it
bcrypt.generate\_password\_hash('testing')<span class="colour" style="color:rgb(212, 212, 212)">.decode(</span><span class="colour" style="color:rgb(206, 145, 120)">'utf-8'</span><span class="colour" style="color:rgb(212, 212, 212)">)</span> --> hashed password with out the b and just a string

1.  Hashing passwords

import Bcrypt and set variable in our init package file
/\_\_init\_\_.py
<span class="colour" style="color:rgb(86, 156, 214)">from</span><span class="colour" style="color:rgb(212, 212, 212)"> flask\_bcrypt </span><span class="colour" style="color:rgb(86, 156, 214)">import</span><span class="colour" style="color:rgb(212, 212, 212)"> Bcrypt</span>
<span class="colour" style="color:rgb(212, 212, 212)">bcrypt = Bcrypt(app)</span>

import bcrypt variable to routes file
/routes.py
from flaskblog import app, db, bcrypt

Here is our revised register route with bcrypt and adding a user to the db
<span class="colour" style="color:rgb(212, 212, 212)">`@app.route(`</span><span class="colour" style="color:rgb(206, 145, 120)">`"/register"`</span><span class="colour" style="color:rgb(212, 212, 212)">`, methods=[`</span><span class="colour" style="color:rgb(206, 145, 120)">`'GET'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, `</span><span class="colour" style="color:rgb(206, 145, 120)">`'POST'`</span><span class="colour" style="color:rgb(212, 212, 212)">`])`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`def`</span><span class="colour" style="color:rgb(212, 212, 212)">` register():`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`    form = RegistrationForm()`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`    if`</span><span class="colour" style="color:rgb(212, 212, 212)">` form.validate_on_submit():`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'utf-8'`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`        new_user = User(username=form.username.data, email=form.email.data, password=hashed_pw)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`        db.session.add(new_user)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`        db.session.commit()`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`        flash(`</span><span class="colour" style="color:rgb(86, 156, 214)">`f`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Your account has been created!  You are able to login,'`</span><span class="colour" style="color:rgb(212, 212, 212)">`success`</span><span class="colour" style="color:rgb(206, 145, 120)">`')`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`        return`</span><span class="colour" style="color:rgb(212, 212, 212)">` redirect(url_for(login))`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`    return`</span><span class="colour" style="color:rgb(212, 212, 212)">` render_template(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'register.html'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, title=`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Register'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, form=form)`</span>

2.  Validate unique username and email

We need to add some validation so that users can't select a username that is taken or email etc.  We can do this in our forms.py

/forms.py

Need validation error from wtforms
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`wtforms.validators`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` ... ValidationError`</span>
Need user model from models
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flaskblog.models`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` User`</span>

`class RegistrationForm(FlaskForm):`
`...`
        <span class="colour" style="color:rgb(86, 156, 214)">`def`</span><span class="colour" style="color:rgb(212, 212, 212)">` validate_username(self, username):`</span>
            <span class="colour" style="color:rgb(212, 212, 212)">`user = User.query.filter_by(username=username.data).first()`</span>
            <span class="colour" style="color:rgb(86, 156, 214)">`if`</span><span class="colour" style="color:rgb(212, 212, 212)">` user:`</span>
                <span class="colour" style="color:rgb(86, 156, 214)">`raise`</span><span class="colour" style="color:rgb(212, 212, 212)">` ValidationError(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'That username is taken.  Please choose a different one'`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>

<span class="colour" style="color:rgb(86, 156, 214)">`    def`</span><span class="colour" style="color:rgb(212, 212, 212)">` validate_email(self, email):`</span>
            <span class="colour" style="color:rgb(212, 212, 212)">`user = User.query.filter_by(email=email.data).first()`</span>
            <span class="colour" style="color:rgb(86, 156, 214)">`if`</span><span class="colour" style="color:rgb(212, 212, 212)">` user:`</span>
                <span class="colour" style="color:rgb(86, 156, 214)">`raise`</span><span class="colour" style="color:rgb(212, 212, 212)">` ValidationError(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'That email is taken.  Please choose a different one'`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>

3.  Login package
This package handles sessions in the background so you don't have to!

% pip install flask-login

/\_\_init\_\_.py

#\_\_\_ imports
from flask\_login import LoginManager
...
#\_\_\_ instances
login\_manager = LoginManager(app)

So now we head on over to our /models.py file and import the login manager from the init file.

/models.py
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flaskblog`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` db, login_manager`</span>

Now in order for us to use the login manager we have to make a function that get's a user id and tag it with the login manager decorator

<span class="colour" style="color:rgb(212, 212, 212)">`@login_manager.user_loader`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`def`</span><span class="colour" style="color:rgb(212, 212, 212)">` load_user(user_id):`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`    return`</span><span class="colour" style="color:rgb(212, 212, 212)">` User.query.get(int(user_id))`</span>

So we need to add 4 methods to our User class but thankfully we can just import them from flask-login
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flask_login`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` UserMixin`</span>

And we have our User model inherit from UserMixin in addition to the db.models
<span class="colour" style="color:rgb(86, 156, 214)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">` User(db.Model, UserMixin):`</span>
    <...>

4.  Login Route

Head on over to routes and lets work on the login route.  First import user\_login

/routes.py
<span class="colour" style="color:rgb(86, 156, 214)">from</span><span class="colour" style="color:rgb(212, 212, 212)"> flask\_login </span><span class="colour" style="color:rgb(86, 156, 214)">import</span><span class="colour" style="color:rgb(212, 212, 212)"> login\_user</span>

<span class="colour" style="color:rgb(212, 212, 212)">#\_\_\_ Now let's look at the login route.  </span>
<span class="colour" style="color:rgb(212, 212, 212)">@app.route(</span><span class="colour" style="color:rgb(206, 145, 120)">"/login"</span><span class="colour" style="color:rgb(212, 212, 212)">, methods=[</span><span class="colour" style="color:rgb(206, 145, 120)">'GET'</span><span class="colour" style="color:rgb(212, 212, 212)">, </span><span class="colour" style="color:rgb(206, 145, 120)">'POST'</span><span class="colour" style="color:rgb(212, 212, 212)">])</span>
<span class="colour" style="color:rgb(86, 156, 214)">def</span><span class="colour" style="color:rgb(212, 212, 212)"> login():</span>
    <span class="colour" style="color:rgb(212, 212, 212)">form = LoginForm()</span>
    <span class="colour" style="color:rgb(86, 156, 214)">if</span><span class="colour" style="color:rgb(212, 212, 212)"> form.validate\_on\_submit():</span>
        <span class="colour" style="color:rgb(212, 212, 212)">user = User.query.filter\_by(email=form.email.data).first()</span>
        <span class="colour" style="color:rgb(86, 156, 214)">if</span><span class="colour" style="color:rgb(212, 212, 212)"> user </span><span class="colour" style="color:rgb(86, 156, 214)">and</span><span class="colour" style="color:rgb(212, 212, 212)"> bcrypt.check\_password\_hash(user.password, form.password.data):</span>
            <span class="colour" style="color:rgb(212, 212, 212)">login\_user(user, remember=form.remember.data)</span>
            <span class="colour" style="color:rgb(86, 156, 214)">return</span><span class="colour" style="color:rgb(212, 212, 212)"> redirect(url\_for(</span><span class="colour" style="color:rgb(206, 145, 120)">'home'</span><span class="colour" style="color:rgb(212, 212, 212)">))</span>
        <span class="colour" style="color:rgb(86, 156, 214)">else</span><span class="colour" style="color:rgb(212, 212, 212)">:</span>
            <span class="colour" style="color:rgb(212, 212, 212)">flash(</span><span class="colour" style="color:rgb(206, 145, 120)">'login uncucessful. Please check email and password'</span><span class="colour" style="color:rgb(212, 212, 212)">, </span><span class="colour" style="color:rgb(206, 145, 120)">'danger'</span><span class="colour" style="color:rgb(212, 212, 212)">)</span>
<span class="colour" style="color:rgb(86, 156, 214)">return</span><span class="colour" style="color:rgb(212, 212, 212)"> render\_template(</span><span class="colour" style="color:rgb(206, 145, 120)">'login.html'</span><span class="colour" style="color:rgb(212, 212, 212)">, title=</span><span class="colour" style="color:rgb(206, 145, 120)">'Login'</span><span class="colour" style="color:rgb(212, 212, 212)">, form=form)</span>

So we grab a user by their email address and save it to a variable called user.  We check that the user exists and if the password is correct in one conditional.  Then we use the login\_user method from flask-login passing the user as an argument and the remember me True or False value as well.  We redirect to Home.  If they have the wrong password or they don't exist, we have an else statement for a flash message.

5.  Hide login and register page if they are logged in

Let's add current\_user to our imports on routes.py
/routes.py
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flask_login`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` login_user, current_user`</span>

Now if someone goes to the register route and they are logged in, it redirects them to the home page.
<span class="colour" style="color:rgb(212, 212, 212)">`@app.route(`</span><span class="colour" style="color:rgb(206, 145, 120)">`"/register"`</span><span class="colour" style="color:rgb(212, 212, 212)">`, methods=[`</span><span class="colour" style="color:rgb(206, 145, 120)">`'GET'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, `</span><span class="colour" style="color:rgb(206, 145, 120)">`'POST'`</span><span class="colour" style="color:rgb(212, 212, 212)">`])`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`def`</span><span class="colour" style="color:rgb(212, 212, 212)">` register():`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`if`</span><span class="colour" style="color:rgb(212, 212, 212)">` current_user.is_authenticated:`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`return`</span><span class="colour" style="color:rgb(212, 212, 212)">` redirect(url_for(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'home'`</span><span class="colour" style="color:rgb(212, 212, 212)">`))`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`...`</span>

6.  Logout Route
Import Logout\_user from flask-login
/routes.py
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flask_login`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` login_user, current_user, logout_user`</span>

and lets look at the logout route
<span class="colour" style="color:rgb(212, 212, 212)">`@app.route(`</span><span class="colour" style="color:rgb(206, 145, 120)">`"/logout"`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`def`</span><span class="colour" style="color:rgb(212, 212, 212)">` logout():`</span>
    <span class="colour" style="color:rgb(212, 212, 212)">`logout_user()`</span>
    <span class="colour" style="color:rgb(86, 156, 214)">`return`</span><span class="colour" style="color:rgb(212, 212, 212)">` redirect(url_for(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'home'`</span><span class="colour" style="color:rgb(212, 212, 212)">`))`</span>

Pretty darn simple.

7.  Navbar hide and show auth routes.
Let's go to our layout.html and put in our conditionals for auth

/layout.html
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`if`</span><span class="colour" style="color:rgb(212, 212, 212)">` current_user.is_authenticated %}`</span>
     <span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`a`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"nav-item nav-link"`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`href`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"{{ url_for('logout') }}"`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span><span class="colour" style="color:rgb(212, 212, 212)">`Logout`</span><span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`a`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`else`</span><span class="colour" style="color:rgb(212, 212, 212)">` %}`</span>
    <span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`a`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"nav-item nav-link"`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`href`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"{{ url_for('login') }}"`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span><span class="colour" style="color:rgb(212, 212, 212)">`Login`</span><span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`a`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
    <span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`a`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"nav-item nav-link"`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`href`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"{{ url_for('register') }}"`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span><span class="colour" style="color:rgb(212, 212, 212)">`Register`</span><span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`a`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`endif`</span><span class="colour" style="color:rgb(212, 212, 212)">` %}`</span>

8.  Block pages from those that are not logged in

We will make an Account route and template to demonstrate
/account.html
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`extends`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(206, 145, 120)">`"layout.html"`</span><span class="colour" style="color:rgb(212, 212, 212)">` %}`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`block`</span><span class="colour" style="color:rgb(212, 212, 212)">` content %}`</span>
<span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`h1`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span><span class="colour" style="color:rgb(212, 212, 212)">`{{ current_user.username }}`</span><span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`h1`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`endblock`</span><span class="colour" style="color:rgb(212, 212, 212)">` content %}`</span>

<span class="colour" style="color:rgb(212, 212, 212)">/layout.html</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`if`</span><span class="colour" style="color:rgb(212, 212, 212)">` current_user.is_authenticated %}`</span>
<span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`a`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"nav-item nav-link"`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`href`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"{{ url_for('logout') }}"`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span><span class="colour" style="color:rgb(212, 212, 212)">`Logout`</span><span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`a`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(128, 128, 128)">`<`</span><span class="colour" style="color:rgb(86, 156, 214)">`a`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`class`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"nav-item nav-link"`</span><span class="colour" style="color:rgb(212, 212, 212)"></span><span class="colour" style="color:rgb(156, 220, 254)">`href`</span><span class="colour" style="color:rgb(212, 212, 212)">`=`</span><span class="colour" style="color:rgb(206, 145, 120)">`"{{ url_for('account') }}"`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span><span class="colour" style="color:rgb(212, 212, 212)">`Account`</span><span class="colour" style="color:rgb(128, 128, 128)">`</`</span><span class="colour" style="color:rgb(86, 156, 214)">`a`</span><span class="colour" style="color:rgb(128, 128, 128)">`>`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`{% `</span><span class="colour" style="color:rgb(86, 156, 214)">`else`</span><span class="colour" style="color:rgb(212, 212, 212)">` %}`</span>
<span class="colour" style="color:rgb(212, 212, 212)">...</span>

/routes.py
Here we use a decorator to check authentication much like django.
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flask_login`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">` <...> login_required`</span>

<span class="colour" style="color:rgb(212, 212, 212)">`@app.route(`</span><span class="colour" style="color:rgb(206, 145, 120)">`"/account"`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>
<span class="colour" style="color:rgb(212, 212, 212)">`@login_required`</span>
<span class="colour" style="color:rgb(86, 156, 214)">`def`</span><span class="colour" style="color:rgb(212, 212, 212)">` account():`</span>
    <span class="colour" style="color:rgb(86, 156, 214)">`return`</span><span class="colour" style="color:rgb(212, 212, 212)">` render_template(`</span><span class="colour" style="color:rgb(206, 145, 120)">`'account.html'`</span><span class="colour" style="color:rgb(212, 212, 212)">`, title=`</span><span class="colour" style="color:rgb(206, 145, 120)">`'Account'`</span><span class="colour" style="color:rgb(212, 212, 212)">`)`</span>

<span class="colour" style="color:rgb(212, 212, 212)">We have to add in our init file the name of our login route for the login manager.</span>

<span class="colour" style="color:rgb(212, 212, 212)">login\_manager = LoginManager(app)</span>
<span class="colour" style="color:rgb(212, 212, 212)">login\_manager.login\_view = </span><span class="colour" style="color:rgb(206, 145, 120)">'login' //--> this is the name of the view function</span>

Now when we go to a page that requires us to be logged in, it redirects us to the login page.

<br>
9.  What if we want to redirect them back to the page that they were on after they login?  Well that is saved in the URL params when they get redirected to the login page.

Need access to request object
/routes.py
<span class="colour" style="color:rgb(86, 156, 214)">`from`</span><span class="colour" style="color:rgb(212, 212, 212)">`flask`</span><span class="colour" style="color:rgb(86, 156, 214)">`import`</span><span class="colour" style="color:rgb(212, 212, 212)">`  <...> request`</span>

def login():
<...>
<br>
```
login_user(user, remember=form.remember.data)
next_page = request.args.get('next')
#___ conditional that checks next page and otherwise routes home
return redirect(nextpage)ifnext_pageelse redirect(url_for('home'))
```

<...>
<br>
# User Account Page and Profile Pic
<br>
Get some fresh html for the account template.  Pass the name of the image file in to the route.  We are also going to make an edit profile form which allows users to upload a picture.  woot.

This is almost the same as our register form but with some things ommitted.  We also run a conditional when validating the username and email.

<span class="colour" style="color: rgb(86, 156, 214);">class</span><span class="colour" style="color: rgb(212, 212, 212);"> UpdateAccountForm(FlaskForm):</span>
<span class="colour" style="color: rgb(212, 212, 212);">username = StringField(</span><span class="colour" style="color: rgb(206, 145, 120);">'Username'</span><span class="colour" style="color: rgb(212, 212, 212);">,</span>
<span class="colour" style="color: rgb(212, 212, 212);">validators=[</span>
<span class="colour" style="color: rgb(212, 212, 212);">DataRequired(),</span>
<span class="colour" style="color: rgb(212, 212, 212);">Length(min=</span><span class="colour" style="color: rgb(181, 206, 168);">2</span><span class="colour" style="color: rgb(212, 212, 212);">, max=</span><span class="colour" style="color: rgb(181, 206, 168);">20</span><span class="colour" style="color: rgb(212, 212, 212);">)])</span>

<span class="colour" style="color: rgb(212, 212, 212);">email = StringField(</span><span class="colour" style="color: rgb(206, 145, 120);">'Email'</span><span class="colour" style="color: rgb(212, 212, 212);">,</span>
<span class="colour" style="color: rgb(212, 212, 212);">validators=[</span>
<span class="colour" style="color: rgb(212, 212, 212);">DataRequired(),</span>
<span class="colour" style="color: rgb(212, 212, 212);">Email()])</span>

<span class="colour" style="color: rgb(212, 212, 212);">submit = SubmitField(</span><span class="colour" style="color: rgb(206, 145, 120);">'Update Account'</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>

<span class="colour" style="color: rgb(86, 156, 214);">def</span><span class="colour" style="color: rgb(212, 212, 212);"> validate\_username(self, username):</span>
<span class="colour" style="color: rgb(86, 156, 214);">if</span><span class="colour" style="color: rgb(212, 212, 212);"> username.data != current\_user.username:</span>
<span class="colour" style="color: rgb(212, 212, 212);">user = User.query.filter\_by(username=username.data).first()</span>
<span class="colour" style="color: rgb(86, 156, 214);">if</span><span class="colour" style="color: rgb(212, 212, 212);"> user:</span>
<span class="colour" style="color: rgb(86, 156, 214);">raise</span><span class="colour" style="color: rgb(212, 212, 212);"> ValidationError(</span><span class="colour" style="color: rgb(206, 145, 120);">'That username is taken. Please choose a different one'</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>

<span class="colour" style="color: rgb(86, 156, 214);">def</span><span class="colour" style="color: rgb(212, 212, 212);"> validate\_email(self, email):</span>
<span class="colour" style="color: rgb(86, 156, 214);">if</span><span class="colour" style="color: rgb(212, 212, 212);"> email.data != current\_user.email:</span>
<span class="colour" style="color: rgb(212, 212, 212);">user = User.query.filter\_by(email=email.data).first()</span>
<span class="colour" style="color: rgb(86, 156, 214);">if</span><span class="colour" style="color: rgb(212, 212, 212);"> user:</span>
<span class="colour" style="color: rgb(86, 156, 214);">raise</span><span class="colour" style="color: rgb(212, 212, 212);"> ValidationError(</span><span class="colour" style="color: rgb(206, 145, 120);">'That email is taken. Please choose a different one'</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>

2.  Update our account route to show form

from flaskblog.forms import UpdateAccountForm()

<span class="colour" style="color: rgb(212, 212, 212);">@app.route(</span><span class="colour" style="color: rgb(206, 145, 120);">"/account"</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>
<span class="colour" style="color: rgb(212, 212, 212);">@login\_required</span>
<span class="colour" style="color: rgb(86, 156, 214);">def</span><span class="colour" style="color: rgb(212, 212, 212);"> account():</span>
<span class="colour" style="color: rgb(212, 212, 212);">form = UpdateAccountForm()</span>
<span class="colour" style="color: rgb(212, 212, 212);">image\_file = url\_for(</span><span class="colour" style="color: rgb(206, 145, 120);">'static'</span><span class="colour" style="color: rgb(212, 212, 212);">, filename=</span><span class="colour" style="color: rgb(206, 145, 120);">'profile\_pics/'</span><span class="colour" style="color: rgb(212, 212, 212);">+current\_user.image\_file)</span>
<span class="colour" style="color: rgb(86, 156, 214);">return</span><span class="colour" style="color: rgb(212, 212, 212);"> render\_template(</span><span class="colour" style="color: rgb(206, 145, 120);">'account.html'</span><span class="colour" style="color: rgb(212, 212, 212);">, title=</span><span class="colour" style="color: rgb(206, 145, 120);">'Account'</span><span class="colour" style="color: rgb(212, 212, 212);">, image\_file=image\_file, form=form)</span>

<span class="colour" style="color: rgb(212, 212, 212);">This will just show the empty form, lots to revise here.  Let's make get and post requests usable.</span>
<span class="colour" style="color: rgb(212, 212, 212);">@app.route(</span><span class="colour" style="color: rgb(206, 145, 120);">"/account"</span><span class="colour" style="color: rgb(212, 212, 212);">, methods=[</span><span class="colour" style="color: rgb(206, 145, 120);">'GET'</span><span class="colour" style="color: rgb(212, 212, 212);">, </span><span class="colour" style="color: rgb(206, 145, 120);">'POST'</span><span class="colour" style="color: rgb(212, 212, 212);">])</span>
<span class="colour" style="color: rgb(212, 212, 212);">@login\_required</span>
<span class="colour" style="color: rgb(86, 156, 214);">def</span><span class="colour" style="color: rgb(212, 212, 212);"> account():</span>
<span class="colour" style="color: rgb(212, 212, 212);">form = UpdateAccountForm()</span>
<span class="colour" style="color: rgb(86, 156, 214);">if</span><span class="colour" style="color: rgb(212, 212, 212);"> form.validate\_on\_submit():</span>
<span class="colour" style="color: rgb(212, 212, 212);">#\_\_\_ updating the User</span>
<span class="colour" style="color: rgb(212, 212, 212);">current\_user.username = form.username.data</span>
<span class="colour" style="color: rgb(212, 212, 212);">current\_user.email = form.email.data</span>
<span class="colour" style="color: rgb(212, 212, 212);">db.session.commit()</span>
<span class="colour" style="color: rgb(212, 212, 212);">flash(</span><span class="colour" style="color: rgb(206, 145, 120);">'Your account has been updated'</span><span class="colour" style="color: rgb(212, 212, 212);">, </span><span class="colour" style="color: rgb(206, 145, 120);">'success'</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>
<span class="colour" style="color: rgb(86, 156, 214);">return</span><span class="colour" style="color: rgb(212, 212, 212);"> redirect(url\_for(</span><span class="colour" style="color: rgb(206, 145, 120);">'account'</span><span class="colour" style="color: rgb(212, 212, 212);">))</span>
<span class="colour" style="color: rgb(212, 212, 212);">#\_\_\_ filling input fields with current user info</span>
<span class="colour" style="color: rgb(86, 156, 214);">elif</span><span class="colour" style="color: rgb(212, 212, 212);"> request.method == </span><span class="colour" style="color: rgb(206, 145, 120);">'GET'</span><span class="colour" style="color: rgb(212, 212, 212);">:</span>
<span class="colour" style="color: rgb(212, 212, 212);">form.username.data = current\_user.username</span>
<span class="colour" style="color: rgb(212, 212, 212);">form.email.data = current\_user.email</span>
<span class="colour" style="color: rgb(212, 212, 212);">image\_file = url\_for(</span><span class="colour" style="color: rgb(206, 145, 120);">'static'</span><span class="colour" style="color: rgb(212, 212, 212);">, filename=</span><span class="colour" style="color: rgb(206, 145, 120);">'profile\_pics/'</span><span class="colour" style="color: rgb(212, 212, 212);">+current\_user.image\_file)</span>
<span class="colour" style="color: rgb(86, 156, 214);">return</span><span class="colour" style="color: rgb(212, 212, 212);"> render\_template(</span><span class="colour" style="color: rgb(206, 145, 120);">'account.html'</span><span class="colour" style="color: rgb(212, 212, 212);">, title=</span><span class="colour" style="color: rgb(206, 145, 120);">'Account'</span><span class="colour" style="color: rgb(212, 212, 212);">, image\_file=image\_file, form=form)</span>

3\. image upload
need to add image to form

first we need to import some dependencies in to this file
<span class="colour" style="color: rgb(86, 156, 214);">`from`</span><span class="colour" style="color: rgb(212, 212, 212);">` flask_wtf.file `</span><span class="colour" style="color: rgb(86, 156, 214);">`import`</span><span class="colour" style="color: rgb(212, 212, 212);">` FileField, FileAllowed`</span>
File allowed is a validator to check what files we want allowed to be uploaded(img only etc)

add this to our update account form:

<span class="colour" style="color: rgb(212, 212, 212);">`picture = FileField(`</span><span class="colour" style="color: rgb(206, 145, 120);">`'Update Profile Picture'`</span><span class="colour" style="color: rgb(212, 212, 212);">`, validators=[FileAllowed([`</span><span class="colour" style="color: rgb(206, 145, 120);">`'jpg'`</span><span class="colour" style="color: rgb(212, 212, 212);">`,`</span><span class="colour" style="color: rgb(206, 145, 120);">`'png'`</span><span class="colour" style="color: rgb(212, 212, 212);">`])])`</span>

Make sure we can see this field on our form in our template and handle errors

We also need to add to our form attributes enctype="multipart/form-data" to accept file inputs
this is a tough one to troubleshoot so don't forget it

4.  Saving an image to the directory and updating the file name

We are going to make a conditional in the route to see if someone is trying to upload a picture.  If they are, then we are going to pass in a function that receives the file, renames to a hex value, and returns the new file name for the database.

/routes.py
imports...
<span class="colour" style="color: rgb(86, 156, 214);">import</span><span class="colour" style="color: rgb(212, 212, 212);"> os --> do useful file and path actions</span>
<span class="colour" style="color: rgb(86, 156, 214);">import</span><span class="colour" style="color: rgb(212, 212, 212);"> secrets //--> we generate random hex with this library</span>

add this function...
<span class="colour" style="color: rgb(86, 156, 214);">def</span><span class="colour" style="color: rgb(212, 212, 212);"> save\_picture(form\_picture):</span>
<span class="colour" style="color: rgb(212, 212, 212);">random\_hex = secrets.token\_hex(</span><span class="colour" style="color: rgb(181, 206, 168);">8</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>
<span class="colour" style="color: rgb(212, 212, 212);">f\_name, f\_ext = os.path.splittext(form\_picture.filename)</span>
<span class="colour" style="color: rgb(212, 212, 212);">picture\_fn = random\_hex + f\_ext</span>
<span class="colour" style="color: rgb(212, 212, 212);">picture\_path = os.path.join(app.root\_path, </span><span class="colour" style="color: rgb(206, 145, 120);">'static/profile\_pics'</span><span class="colour" style="color: rgb(212, 212, 212);">, picture\_fn)</span>
<span class="colour" style="color: rgb(212, 212, 212);">form\_picture.save(picture\_path)</span>
<span class="colour" style="color: rgb(86, 156, 214);">return</span><span class="colour" style="color: rgb(212, 212, 212);"> picture\_fn</span>

update profile route:
<...>
<span class="colour" style="color: rgb(86, 156, 214);">if</span><span class="colour" style="color: rgb(212, 212, 212);"> form.picture.data:</span>
<span class="colour" style="color: rgb(212, 212, 212);">picture\_file = save\_picture(form.picture.data)</span>
<span class="colour" style="color: rgb(212, 212, 212);">current\_user.image\_file = picture\_file</span>
<span class="colour" style="color: rgb(212, 212, 212);"><...></span>

5.  Resizing incoming pictures
Pillow is the package to resize the image.

% pip install Pillow

/routes.py
from PIL import Image

Modify our picture download function

<span class="colour" style="color: rgb(86, 156, 214);">def</span><span class="colour" style="color: rgb(212, 212, 212);"> save\_picture(form\_picture):</span>
<span class="colour" style="color: rgb(212, 212, 212);">random\_hex = secrets.token\_hex(</span><span class="colour" style="color: rgb(181, 206, 168);">8</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>
<span class="colour" style="color: rgb(212, 212, 212);">f\_name, f\_ext = os.path.splittext(form\_picture.filename)</span>
<span class="colour" style="color: rgb(212, 212, 212);">picture\_fn = random\_hex + f\_ext</span>
<span class="colour" style="color: rgb(212, 212, 212);">picture\_path = os.path.join(app.root\_path, </span><span class="colour" style="color: rgb(206, 145, 120);">'static/profile\_pics'</span><span class="colour" style="color: rgb(212, 212, 212);">, picture\_fn)</span>
<span class="colour" style="color: rgb(212, 212, 212);">#\_\_\_ new shit starts here</span>
<span class="colour" style="color: rgb(212, 212, 212);">output\_size = (</span><span class="colour" style="color: rgb(181, 206, 168);">125</span><span class="colour" style="color: rgb(212, 212, 212);">, </span><span class="colour" style="color: rgb(181, 206, 168);">125</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>
<span class="colour" style="color: rgb(212, 212, 212);">i = Image.open(form\_picture)</span>
<span class="colour" style="color: rgb(212, 212, 212);">i.thumbnail(output\_size)</span>
<span class="colour" style="color: rgb(212, 212, 212);">i.save(picture\_path)</span>
<span class="colour" style="color: rgb(86, 156, 214);">return</span><span class="colour" style="color: rgb(212, 212, 212);"> picture\_fn</span>

<br>
# CRUD on Posts Model
<br>
Goodbye Dummy Data!!!

1.  Need to create a new post route, template, form, and a link to the create post form.

/forms.py
<span class="colour" style="color: rgb(86, 156, 214);">from</span><span class="colour" style="color: rgb(212, 212, 212);"> wtforms </span><span class="colour" style="color: rgb(86, 156, 214);">import</span><span class="colour" style="color: rgb(212, 212, 212);"> ....TextAreaField</span>
<...>
<span class="colour" style="color: rgb(86, 156, 214);">class</span><span class="colour" style="color: rgb(212, 212, 212);"> PostForm(FlaskForm):</span>
<span class="colour" style="color: rgb(212, 212, 212);">title = StringField(</span><span class="colour" style="color: rgb(206, 145, 120);">'Title'</span><span class="colour" style="color: rgb(212, 212, 212);">, validators=[DataRequired()])</span>
<span class="colour" style="color: rgb(212, 212, 212);">content = TextAreaField(</span><span class="colour" style="color: rgb(206, 145, 120);">'Content'</span><span class="colour" style="color: rgb(212, 212, 212);">, validators[DataRequired()])</span>
<span class="colour" style="color: rgb(212, 212, 212);">submit = SubmitField(</span><span class="colour" style="color: rgb(206, 145, 120);">'Post'</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>

/layout.html
<span class="colour" style="color: rgb(128, 128, 128);"><</span><span class="colour" style="color: rgb(86, 156, 214);">a</span><span class="colour" style="color: rgb(212, 212, 212);"> </span><span class="colour" style="color: rgb(156, 220, 254);">class</span><span class="colour" style="color: rgb(212, 212, 212);">=</span><span class="colour" style="color: rgb(206, 145, 120);">"nav-item nav-link"</span><span class="colour" style="color: rgb(212, 212, 212);"> </span><span class="colour" style="color: rgb(156, 220, 254);">href</span><span class="colour" style="color: rgb(212, 212, 212);">=</span><span class="colour" style="color: rgb(206, 145, 120);">"{{ url\_for('new\_post') }}"</span><span class="colour" style="color: rgb(128, 128, 128);">></span><span class="colour" style="color: rgb(212, 212, 212);">New Post</span><span class="colour" style="color: rgb(128, 128, 128);"></</span><span class="colour" style="color: rgb(86, 156, 214);">a</span><span class="colour" style="color: rgb(128, 128, 128);">></span>

/routes.py
<span class="colour" style="color: rgb(86, 156, 214);">from</span><span class="colour" style="color: rgb(212, 212, 212);"> flaskblog.forms </span><span class="colour" style="color: rgb(86, 156, 214);">import</span><span class="colour" style="color: rgb(212, 212, 212);"> ... PostForm</span>

New Post Route

<span class="colour" style="color: rgb(212, 212, 212);">@app.route(</span><span class="colour" style="color: rgb(206, 145, 120);">"/post/new"</span><span class="colour" style="color: rgb(212, 212, 212);">, methods=[</span><span class="colour" style="color: rgb(206, 145, 120);">'GET'</span><span class="colour" style="color: rgb(212, 212, 212);">,</span><span class="colour" style="color: rgb(206, 145, 120);">'POST'</span><span class="colour" style="color: rgb(212, 212, 212);">])</span>
<span class="colour" style="color: rgb(212, 212, 212);">@login\_required</span>
<span class="colour" style="color: rgb(86, 156, 214);">def</span><span class="colour" style="color: rgb(212, 212, 212);"> new\_post():</span>
<span class="colour" style="color: rgb(212, 212, 212);">    form = PostForm()</span>
<span class="colour" style="color: rgb(86, 156, 214);">    if</span><span class="colour" style="color: rgb(212, 212, 212);"> form.validate\_on\_submit():</span>
<span class="colour" style="color: rgb(212, 212, 212);">        new\_p = Post(</span>
<span class="colour" style="color: rgb(212, 212, 212);">           title=form.title.data,</span>
<span class="colour" style="color: rgb(212, 212, 212);">           content=form.content.data,</span>
<span class="colour" style="color: rgb(212, 212, 212);">           author=current\_user )</span>
<span class="colour" style="color: rgb(212, 212, 212);">           db.session.add(new\_p)</span>
<span class="colour" style="color: rgb(212, 212, 212);">           db.session.commit()</span>
<span class="colour" style="color: rgb(212, 212, 212);">           flash(</span><span class="colour" style="color: rgb(206, 145, 120);">'Your post has been created!'</span><span class="colour" style="color: rgb(212, 212, 212);">, </span><span class="colour" style="color: rgb(206, 145, 120);">'success'</span><span class="colour" style="color: rgb(212, 212, 212);"> )</span>
<span class="colour" style="color: rgb(212, 212, 212);">           </span><span class="colour" style="color: rgb(86, 156, 214);">return</span><span class="colour" style="color: rgb(212, 212, 212);"> redirect(url\_for(</span><span class="colour" style="color: rgb(206, 145, 120);">'home'</span><span class="colour" style="color: rgb(212, 212, 212);">))</span>
<span class="colour" style="color: rgb(86, 156, 214);">    return</span><span class="colour" style="color: rgb(212, 212, 212);"> render\_template(</span><span class="colour" style="color: rgb(206, 145, 120);">'create\_post.html'</span><span class="colour" style="color: rgb(212, 212, 212);">, title=</span><span class="colour" style="color: rgb(206, 145, 120);">'New Post'</span><span class="colour" style="color: rgb(212, 212, 212);">, form=form)</span>

Adjust the home page to display the posts better

2.  Post Show Page
We can pass a variable in to the url pattern
@app.route("/post/<post\_id>")
We can also designate an integer with int:
@app.route("/post/<int:post\_id>")

We can pass ids in our url\_for function url\_for('post', post\_id=post.id)

we also have a new query that is Post.query.get\_or\_404(post.id)... if there are not any posts you get a 404 error.

The Route:
<span class="colour" style="color: rgb(212, 212, 212);">@app.route(</span><span class="colour" style="color: rgb(206, 145, 120);">"/post/<int:post\_id>"</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>
<span class="colour" style="color: rgb(86, 156, 214);">def</span><span class="colour" style="color: rgb(212, 212, 212);"> post(post\_id):</span>
<span class="colour" style="color: rgb(212, 212, 212);">post = Post.query.get\_or\_404(post\_id)</span>
<span class="colour" style="color: rgb(86, 156, 214);">return</span><span class="colour" style="color: rgb(212, 212, 212);"> render\_template(</span><span class="colour" style="color: rgb(206, 145, 120);">'post.html'</span><span class="colour" style="color: rgb(212, 212, 212);">, title=post.title, post=post)</span>

3.  Update Post

import abort from flask
<span class="colour" style="color: rgb(86, 156, 214);">from</span><span class="colour" style="color: rgb(212, 212, 212);"> flask </span><span class="colour" style="color: rgb(86, 156, 214);">import </span><span class="colour" style="color: rgb(212, 212, 212);">... abort</span>

This will allow us to abort the request if a user is trying to edit another user's post.

<span class="colour" style="color: rgb(212, 212, 212);">@login\_required</span>
<span class="colour" style="color: rgb(212, 212, 212);">@app.route(</span><span class="colour" style="color: rgb(206, 145, 120);">"/post/<int:post\_id>/update"</span><span class="colour" style="color: rgb(212, 212, 212);">,, methods=[</span><span class="colour" style="color: rgb(206, 145, 120);">'GET'</span><span class="colour" style="color: rgb(212, 212, 212);">,</span><span class="colour" style="color: rgb(206, 145, 120);">'POST'</span><span class="colour" style="color: rgb(212, 212, 212);">])</span>
<span class="colour" style="color: rgb(86, 156, 214);">def</span><span class="colour" style="color: rgb(212, 212, 212);"> update\_post(post\_id):</span>
    <span class="colour" style="color: rgb(212, 212, 212);">post = Post.query.get\_or\_404(post\_id)</span>
    <span class="colour" style="color: rgb(86, 156, 214);">if</span><span class="colour" style="color: rgb(212, 212, 212);"> post.author != current\_user:</span>
        <span class="colour" style="color: rgb(212, 212, 212);">abort(</span><span class="colour" style="color: rgb(181, 206, 168);">403</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>
    <span class="colour" style="color: rgb(212, 212, 212);">form = PostForm()</span>
    <span class="colour" style="color: rgb(86, 156, 214);">if</span><span class="colour" style="color: rgb(212, 212, 212);"> form.validate\_on\_submit():</span>
        <span class="colour" style="color: rgb(212, 212, 212);">post.title = form.title.data</span>
        <span class="colour" style="color: rgb(212, 212, 212);">post.content = form.content.data</span>
        <span class="colour" style="color: rgb(212, 212, 212);">db.session.commit()</span>
        <span class="colour" style="color: rgb(212, 212, 212);">flash(</span><span class="colour" style="color: rgb(206, 145, 120);">'Your post has been updated'</span><span class="colour" style="color: rgb(212, 212, 212);">, </span><span class="colour" style="color: rgb(206, 145, 120);">'success'</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>
        <span class="colour" style="color: rgb(86, 156, 214);">return</span><span class="colour" style="color: rgb(212, 212, 212);"> redirect(url\_for(</span><span class="colour" style="color: rgb(206, 145, 120);">'post'</span><span class="colour" style="color: rgb(212, 212, 212);">, post\_id=post.id))</span>
    <span class="colour" style="color: rgb(86, 156, 214);">elif</span><span class="colour" style="color: rgb(212, 212, 212);"> request.method == </span><span class="colour" style="color: rgb(206, 145, 120);">'GET'</span><span class="colour" style="color: rgb(212, 212, 212);">:</span>
        <span class="colour" style="color: rgb(212, 212, 212);">form.title.data = post.title</span>
        <span class="colour" style="color: rgb(212, 212, 212);">form.content.data = post.content</span>
    <span class="colour" style="color: rgb(86, 156, 214);">return</span><span class="colour" style="color: rgb(212, 212, 212);"> render\_template(</span><span class="colour" style="color: rgb(206, 145, 120);">'create\_post.html'</span><span class="colour" style="color: rgb(212, 212, 212);">, title=</span><span class="colour" style="color: rgb(206, 145, 120);">'Update Post'</span><span class="colour" style="color: rgb(212, 212, 212);">, legend=</span><span class="colour" style="color: rgb(206, 145, 120);">'Update Post'</span><span class="colour" style="color: rgb(212, 212, 212);">, form=form)</span>

<br>
<br>
<br>
<br>
