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
<span class="colour" style="color:rgb(106, 153, 85)">#\_\_\_ Import Module</span>

<span class="colour" style="color:rgb(86, 156, 214)">from</span><span class="colour" style="color:rgb(212, 212, 212)"> flask\_wtf </span><span class="colour" style="color:rgb(86, 156, 214)">import</span><span class="colour" style="color:rgb(212, 212, 212)"> FlaskForm</span>
<span class="colour" style="color:rgb(106, 153, 85)">#\_\_\_ Form Fields</span>
<span class="colour" style="color:rgb(86, 156, 214)">from</span><span class="colour" style="color:rgb(212, 212, 212)"> wtforms </span><span class="colour" style="color:rgb(86, 156, 214)">import</span><span class="colour" style="color:rgb(212, 212, 212)"> StringField, PasswordField, SubmitField, BooleanField</span>
<span class="colour" style="color:rgb(106, 153, 85)">#\_\_\_ Validators</span>
<span class="colour" style="color:rgb(86, 156, 214)">from</span><span class="colour" style="color:rgb(212, 212, 212)"> wtforms.validators </span><span class="colour" style="color:rgb(86, 156, 214)">import</span><span class="colour" style="color:rgb(212, 212, 212)"> DataRequired, Length, Email, EqualTo</span>

When writing your input you select a field, you give it a name for the class and then the first argument is a string that will be the label for that input.  Next you can add your validators in an array, make sure you invoke them.  DataRequired means they can't leave it blank, Length takes two kwargs min and max, Email checks for valid email address, and EqualTo allows you to compare the two password fields and make sure they match.

Registration Form:

<span class="colour" style="color:rgb(86, 156, 214)">class</span><span class="colour" style="color:rgb(212, 212, 212)"> RegistrationForm(FlaskForm):</span>

<span class="colour" style="color:rgb(212, 212, 212)">username = StringField(</span><span class="colour" style="color:rgb(206, 145, 120)">'Username'</span><span class="colour" style="color:rgb(212, 212, 212)">,</span>
<span class="colour" style="color:rgb(212, 212, 212)">validators=[</span>
<span class="colour" style="color:rgb(212, 212, 212)">DataRequired(),</span>
<span class="colour" style="color:rgb(212, 212, 212)">Length(min=</span><span class="colour" style="color:rgb(181, 206, 168)">2</span><span class="colour" style="color:rgb(212, 212, 212)">, max=</span><span class="colour" style="color:rgb(181, 206, 168)">20</span><span class="colour" style="color:rgb(212, 212, 212)">)]),</span>

<span class="colour" style="color:rgb(212, 212, 212)">email = StringField(</span><span class="colour" style="color:rgb(206, 145, 120)">'Email'</span><span class="colour" style="color:rgb(212, 212, 212)">,</span>
<span class="colour" style="color:rgb(212, 212, 212)">validators=[</span>
<span class="colour" style="color:rgb(212, 212, 212)">DataRequired(),</span>
<span class="colour" style="color:rgb(212, 212, 212)">Email()]),</span>

<span class="colour" style="color:rgb(212, 212, 212)">password = PasswordField(</span><span class="colour" style="color:rgb(206, 145, 120)">'Password'</span><span class="colour" style="color:rgb(212, 212, 212)">,</span>
<span class="colour" style="color:rgb(212, 212, 212)">validators=</span>
<span class="colour" style="color:rgb(212, 212, 212)">DataRequired()),</span>

<span class="colour" style="color:rgb(212, 212, 212)">confirm\_password = PasswordField(</span><span class="colour" style="color:rgb(206, 145, 120)">'Confirm Password'</span><span class="colour" style="color:rgb(212, 212, 212)">,</span>
<span class="colour" style="color:rgb(212, 212, 212)">validators=[</span>
<span class="colour" style="color:rgb(212, 212, 212)">DataRequired(),</span>
<span class="colour" style="color:rgb(212, 212, 212)">EqualTo(</span><span class="colour" style="color:rgb(206, 145, 120)">'password'</span><span class="colour" style="color:rgb(212, 212, 212)">)])</span>

<span class="colour" style="color:rgb(212, 212, 212)">submit = SubmitField(</span><span class="colour" style="color:rgb(206, 145, 120)">'Sign Up'</span><span class="colour" style="color:rgb(212, 212, 212)">)</span>

2\. Secret Key

Add a secret key to your flaskblog.py file

<span class="colour" style="color:rgb(212, 212, 212)">app.config[</span><span class="colour" style="color:rgb(206, 145, 120)">'SECRET\_KEY'</span><span class="colour" style="color:rgb(212, 212, 212)"> = </span><span class="colour" style="color:rgb(206, 145, 120)">' < top secret key goes here > '</span><span class="colour" style="color:rgb(212, 212, 212)">]</span>

3.  Import forms in to flaskblog.py

/flaskblog.py
<span class="colour" style="color:rgb(86, 156, 214)">from</span><span class="colour" style="color:rgb(212, 212, 212)"> forms </span><span class="colour" style="color:rgb(86, 156, 214)">import</span><span class="colour" style="color:rgb(212, 212, 212)"> RegistrationForm, LoginForm</span>

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

Label - <span class="colour" style="color: rgb(212, 212, 212);">`{{ form.username.label(class=`</span><span class="colour" style="color: rgb(206, 145, 120);">`"classes-go-here"`</span><span class="colour" style="color: rgb(212, 212, 212);">`) }}`</span>

<span class="colour" style="color: rgb(212, 212, 212);">Field - `{{ form.username(class=`</span><span class="colour" style="color: rgb(206, 145, 120);">`"classes-go-here"`</span><span class="colour" style="color: rgb(212, 212, 212);">`) }}`</span>

6.  POST requests...

We need to modify the app.route decorator for the destination of our form submission otherwise we get an error that you cannot POST to that URL.

<span class="colour" style="color: rgb(212, 212, 212);">`@app.route(`</span><span class="colour" style="color: rgb(206, 145, 120);">`"/register"`</span><span class="colour" style="color: rgb(212, 212, 212);">`, methods=[`</span><span class="colour" style="color: rgb(206, 145, 120);">`'GET'`</span><span class="colour" style="color: rgb(212, 212, 212);">`, `</span><span class="colour" style="color: rgb(206, 145, 120);">`'POST'`</span><span class="colour" style="color: rgb(212, 212, 212);">`])`</span>

<br>
7.  Form Validation

In our POST route we can validate the incoming form and for now we pass a flash message to confirm post.
<span class="colour" style="color: rgb(86, 156, 214);">`if`</span><span class="colour" style="color: rgb(212, 212, 212);">` form.validate_on_submit():`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`flash(`</span><span class="colour" style="color: rgb(86, 156, 214);">`f`</span><span class="colour" style="color: rgb(206, 145, 120);">`'Account created for `</span><span class="colour" style="color: rgb(212, 212, 212);">`{form.username.data}`</span><span class="colour" style="color: rgb(206, 145, 120);">`!'`</span><span class="colour" style="color: rgb(212, 212, 212);">`)`</span>

<span class="colour" style="color: rgb(212, 212, 212);">make sure to import flash</span>
<span class="colour" style="color: rgb(86, 156, 214);">`from`</span><span class="colour" style="color: rgb(212, 212, 212);">` flask `</span><span class="colour" style="color: rgb(86, 156, 214);">`import`</span><span class="colour" style="color: rgb(212, 212, 212);">` Flask, render_template, url_for, flash`</span>

Now if we want to see these messages in the browser we have to put some html in to our layout template.  We can also pass in a class by using the category argument in the flash function
<span class="colour" style="color: rgb(212, 212, 212);">`flash(`</span><span class="colour" style="color: rgb(86, 156, 214);">`f`</span><span class="colour" style="color: rgb(206, 145, 120);">`'Account created for `</span><span class="colour" style="color: rgb(212, 212, 212);">`{form.username.data}`</span><span class="colour" style="color: rgb(206, 145, 120);">`!', 'success'`</span><span class="colour" style="color: rgb(212, 212, 212);">`)`</span>

So here we are passing the word success in as the message category and we can then use that as a class to style the message.  So success could be gree/blue and invalid can be red or whatever.

<br>
/layout.html
<span class="colour" style="color: rgb(212, 212, 212);">`{% `</span><span class="colour" style="color: rgb(86, 156, 214);">`with`</span><span class="colour" style="color: rgb(212, 212, 212);">` messages = get_flashed_messages(with_categories=`</span><span class="colour" style="color: rgb(86, 156, 214);">`true`</span><span class="colour" style="color: rgb(212, 212, 212);">`) %}`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{% `</span><span class="colour" style="color: rgb(86, 156, 214);">`if`</span><span class="colour" style="color: rgb(212, 212, 212);">` messages %}`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{% `</span><span class="colour" style="color: rgb(86, 156, 214);">`for`</span><span class="colour" style="color: rgb(212, 212, 212);">` category, message `</span><span class="colour" style="color: rgb(86, 156, 214);">`in`</span><span class="colour" style="color: rgb(212, 212, 212);">` messages %}`</span>
<span class="colour" style="color: rgb(128, 128, 128);">`<`</span><span class="colour" style="color: rgb(86, 156, 214);">`div`</span><span class="colour" style="color: rgb(212, 212, 212);"></span><span class="colour" style="color: rgb(156, 220, 254);">`class`</span><span class="colour" style="color: rgb(212, 212, 212);">`=`</span><span class="colour" style="color: rgb(206, 145, 120);">`"alert alert-{{ category }}"`</span><span class="colour" style="color: rgb(128, 128, 128);">`>`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{{ message }}`</span>
<span class="colour" style="color: rgb(128, 128, 128);">`</`</span><span class="colour" style="color: rgb(86, 156, 214);">`div`</span><span class="colour" style="color: rgb(128, 128, 128);">`>`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{% `</span><span class="colour" style="color: rgb(86, 156, 214);">`endfor`</span><span class="colour" style="color: rgb(212, 212, 212);">` %}`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{% `</span><span class="colour" style="color: rgb(86, 156, 214);">`endif`</span><span class="colour" style="color: rgb(212, 212, 212);">` %}`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{% `</span><span class="colour" style="color: rgb(86, 156, 214);">`endwith`</span><span class="colour" style="color: rgb(212, 212, 212);">` %}`</span>

8\. User Validation in the HTML form

It would be better if the user got feedback while filling out the form instead of waiting for submit.  Also, it takes some of the weight off of our server and utilizes their browser.

One Example in /register.html
<span class="colour" style="color: rgb(128, 128, 128);">`<`</span><span class="colour" style="color: rgb(86, 156, 214);">`div`</span><span class="colour" style="color: rgb(212, 212, 212);"></span><span class="colour" style="color: rgb(156, 220, 254);">`class`</span><span class="colour" style="color: rgb(212, 212, 212);">`=`</span><span class="colour" style="color: rgb(206, 145, 120);">`"form-group"`</span><span class="colour" style="color: rgb(128, 128, 128);">`>`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{{ form.username.label(class=`</span><span class="colour" style="color: rgb(206, 145, 120);">`"form-control-label"`</span><span class="colour" style="color: rgb(212, 212, 212);">`) }}`</span>

<span class="colour" style="color: rgb(212, 212, 212);">`{% `</span><span class="colour" style="color: rgb(86, 156, 214);">`if`</span><span class="colour" style="color: rgb(212, 212, 212);">` form.username.errors %}`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{{ form.username(class=`</span><span class="colour" style="color: rgb(206, 145, 120);">`"form-control form-control-lg is-invalid"`</span><span class="colour" style="color: rgb(212, 212, 212);">`) }}`</span>
<span class="colour" style="color: rgb(128, 128, 128);">`<`</span><span class="colour" style="color: rgb(86, 156, 214);">`div`</span><span class="colour" style="color: rgb(212, 212, 212);"></span><span class="colour" style="color: rgb(156, 220, 254);">`class`</span><span class="colour" style="color: rgb(212, 212, 212);">`=`</span><span class="colour" style="color: rgb(206, 145, 120);">`"invalid-feedback"`</span><span class="colour" style="color: rgb(128, 128, 128);">`>`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{% `</span><span class="colour" style="color: rgb(86, 156, 214);">`for`</span><span class="colour" style="color: rgb(212, 212, 212);">` error `</span><span class="colour" style="color: rgb(86, 156, 214);">`in`</span><span class="colour" style="color: rgb(212, 212, 212);">` form.username.errors %}`</span>
<span class="colour" style="color: rgb(128, 128, 128);">`<`</span><span class="colour" style="color: rgb(86, 156, 214);">`span`</span><span class="colour" style="color: rgb(128, 128, 128);">`>`</span><span class="colour" style="color: rgb(212, 212, 212);">`{{ error }}`</span><span class="colour" style="color: rgb(128, 128, 128);">`</`</span><span class="colour" style="color: rgb(86, 156, 214);">`span`</span><span class="colour" style="color: rgb(128, 128, 128);">`>`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{% `</span><span class="colour" style="color: rgb(86, 156, 214);">`endfor`</span><span class="colour" style="color: rgb(212, 212, 212);">` %}`</span>
<span class="colour" style="color: rgb(128, 128, 128);">`</`</span><span class="colour" style="color: rgb(86, 156, 214);">`div`</span><span class="colour" style="color: rgb(128, 128, 128);">`>`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{% `</span><span class="colour" style="color: rgb(86, 156, 214);">`else`</span><span class="colour" style="color: rgb(212, 212, 212);">` %}`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{{ form.username(class=`</span><span class="colour" style="color: rgb(206, 145, 120);">`"form-control form-control-lg"`</span><span class="colour" style="color: rgb(212, 212, 212);">`) }}`</span>
<span class="colour" style="color: rgb(212, 212, 212);">`{% `</span><span class="colour" style="color: rgb(86, 156, 214);">`endif`</span><span class="colour" style="color: rgb(212, 212, 212);">` %}`</span>
<span class="colour" style="color: rgb(128, 128, 128);">`</`</span><span class="colour" style="color: rgb(86, 156, 214);">`div`</span><span class="colour" style="color: rgb(128, 128, 128);">`>`</span>

For login we copy and paste and modify.  The route for login will have to wait until database is up and running.
For the sake of an example to test we put in a hardcoded user info to test the validation messages.

9.  Nav Bar clean up, we can use url\_for() to pass routes in to links in our nav bar.
<span class="colour" style="color: rgb(128, 128, 128);">`<`</span><span class="colour" style="color: rgb(86, 156, 214);">`a `</span><span class="colour" style="color: rgb(156, 220, 254);">`href`</span><span class="colour" style="color: rgb(212, 212, 212);">`=`</span><span class="colour" style="color: rgb(206, 145, 120);">`"{{ url_for('about') }}"`</span><span class="colour" style="color: rgb(128, 128, 128);">`>`</span><span class="colour" style="color: rgb(212, 212, 212);">`About`</span><span class="colour" style="color: rgb(128, 128, 128);">`</`</span><span class="colour" style="color: rgb(86, 156, 214);">`a`</span><span class="colour" style="color: rgb(128, 128, 128);">`>`</span>
<br>
# Database with Flask-SQL-Alchmey

SQL Alchemy is an ORM, object relational mapper.  Makes it much easier to work with SQL.  Just like Mongoose for MongoDB.

Install flask sql alchemy

`% pip install flask-sqlalchemy`

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
