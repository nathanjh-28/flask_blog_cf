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
<span class="colour" style="color: rgb(86, 156, 214);">from</span><span class="colour" style="color: rgb(212, 212, 212);"> flask </span><span class="colour" style="color: rgb(86, 156, 214);">import</span><span class="colour" style="color: rgb(212, 212, 212);"> Flask, render\_template</span>
And now we can return the function of render\_template with the argument of the name of the html file.
<span class="colour" style="color: rgb(86, 156, 214);">return</span><span class="colour" style="color: rgb(212, 212, 212);"> render\_template(</span><span class="colour" style="color: rgb(206, 145, 120);">'home.html'</span><span class="colour" style="color: rgb(212, 212, 212);">)</span>
4\. Showing data in Templates\.\.\. We can get started by writng some "dummy data" in our flaskblog\.py file\.
<span class="colour" style="color: rgb(106, 153, 85);">#\_\_ "dummy" data</span>
<span class="colour" style="color: rgb(212, 212, 212);">posts = [</span>
<span class="colour" style="color: rgb(212, 212, 212);">{</span>
<span class="colour" style="color: rgb(206, 145, 120);">'author'</span><span class="colour" style="color: rgb(212, 212, 212);">: </span><span class="colour" style="color: rgb(206, 145, 120);">'Nathan Harris'</span><span class="colour" style="color: rgb(212, 212, 212);">,</span>
<span class="colour" style="color: rgb(206, 145, 120);">'title'</span><span class="colour" style="color: rgb(212, 212, 212);">: </span><span class="colour" style="color: rgb(206, 145, 120);">'Blog Post 1'</span><span class="colour" style="color: rgb(212, 212, 212);">,</span>
<span class="colour" style="color: rgb(206, 145, 120);">'content'</span><span class="colour" style="color: rgb(212, 212, 212);">: </span><span class="colour" style="color: rgb(206, 145, 120);">'Lorem Ipsum blah blah blah'</span><span class="colour" style="color: rgb(212, 212, 212);">,</span>
<span class="colour" style="color: rgb(206, 145, 120);">'date\_posted'</span><span class="colour" style="color: rgb(212, 212, 212);">: </span><span class="colour" style="color: rgb(206, 145, 120);">'April 20, 2018'</span>
<span class="colour" style="color: rgb(212, 212, 212);">},</span>
<span class="colour" style="color: rgb(212, 212, 212);">{</span>
<span class="colour" style="color: rgb(206, 145, 120);">'author'</span><span class="colour" style="color: rgb(212, 212, 212);">: </span><span class="colour" style="color: rgb(206, 145, 120);">'Jeff Smitty'</span><span class="colour" style="color: rgb(212, 212, 212);">,</span>
<span class="colour" style="color: rgb(206, 145, 120);">'title'</span><span class="colour" style="color: rgb(212, 212, 212);">: </span><span class="colour" style="color: rgb(206, 145, 120);">'Blog Post 2'</span><span class="colour" style="color: rgb(212, 212, 212);">,</span>
<span class="colour" style="color: rgb(206, 145, 120);">'content'</span><span class="colour" style="color: rgb(212, 212, 212);">: </span><span class="colour" style="color: rgb(206, 145, 120);">'hello world my name is Jeffff and I like to party!'</span><span class="colour" style="color: rgb(212, 212, 212);">,</span>
<span class="colour" style="color: rgb(206, 145, 120);">'date\_posted'</span><span class="colour" style="color: rgb(212, 212, 212);">: </span><span class="colour" style="color: rgb(206, 145, 120);">'May 1, 2018'</span>
<span class="colour" style="color: rgb(212, 212, 212);">}</span>
<span class="colour" style="color: rgb(212, 212, 212);">]</span>

To pass this data in to our template we add a second argument to the render\_template function and write a kwarg... posts=posts.  the first posts refers to the data in the template and the second refers to the data in this file.

5.  We can use Jinja2 logic in our html template files to loop through data or use conditionals to hide and show data.
{% logic goes in between these tags %}
{{ content goes in between these tags }}
To write a for loop (and other things) you have to make an ending tag for it.  {% endfor %}

<span class="colour" style="color: rgb(212, 212, 212);">{% </span><span class="colour" style="color: rgb(86, 156, 214);">for</span><span class="colour" style="color: rgb(212, 212, 212);"> post </span><span class="colour" style="color: rgb(86, 156, 214);">in</span><span class="colour" style="color: rgb(212, 212, 212);"> posts %}</span>
<span class="colour" style="color: rgb(128, 128, 128);"><</span><span class="colour" style="color: rgb(86, 156, 214);">h3</span><span class="colour" style="color: rgb(128, 128, 128);">></span><span class="colour" style="color: rgb(212, 212, 212);">{{ post.title }}</span><span class="colour" style="color: rgb(128, 128, 128);"></</span><span class="colour" style="color: rgb(86, 156, 214);">h3</span><span class="colour" style="color: rgb(128, 128, 128);">></span>
<span class="colour" style="color: rgb(128, 128, 128);"><</span><span class="colour" style="color: rgb(86, 156, 214);">h4</span><span class="colour" style="color: rgb(128, 128, 128);">></span><span class="colour" style="color: rgb(212, 212, 212);">By {{ post.author }} on {{ post.date\_posted }}</span><span class="colour" style="color: rgb(128, 128, 128);"></</span><span class="colour" style="color: rgb(86, 156, 214);">h4</span><span class="colour" style="color: rgb(128, 128, 128);">></span>
<span class="colour" style="color: rgb(128, 128, 128);"><</span><span class="colour" style="color: rgb(86, 156, 214);">p</span><span class="colour" style="color: rgb(128, 128, 128);">></span><span class="colour" style="color: rgb(212, 212, 212);">{{ post.content }}</span><span class="colour" style="color: rgb(128, 128, 128);"></</span><span class="colour" style="color: rgb(86, 156, 214);">p</span><span class="colour" style="color: rgb(128, 128, 128);">></span>
<span class="colour" style="color: rgb(212, 212, 212);">{% </span><span class="colour" style="color: rgb(86, 156, 214);">endfor</span><span class="colour" style="color: rgb(212, 212, 212);"> %}</span>

6.  Conditionals are written like this:  {% if something%} do this {% else %} other things {% endif %}.  Don't forget the endif otherwise you get an error.

<span class="colour" style="color: rgb(212, 212, 212);">{% </span><span class="colour" style="color: rgb(86, 156, 214);">if</span><span class="colour" style="color: rgb(212, 212, 212);"> title %}</span>
<span class="colour" style="color: rgb(128, 128, 128);"><</span><span class="colour" style="color: rgb(86, 156, 214);">title</span><span class="colour" style="color: rgb(128, 128, 128);">></span><span class="colour" style="color: rgb(212, 212, 212);">Flask Blog - {{ title }}</span><span class="colour" style="color: rgb(128, 128, 128);"></</span><span class="colour" style="color: rgb(86, 156, 214);">title</span><span class="colour" style="color: rgb(128, 128, 128);">></span>
<span class="colour" style="color: rgb(212, 212, 212);">{% </span><span class="colour" style="color: rgb(86, 156, 214);">else</span><span class="colour" style="color: rgb(212, 212, 212);"> %}</span>
<span class="colour" style="color: rgb(128, 128, 128);"><</span><span class="colour" style="color: rgb(86, 156, 214);">title</span><span class="colour" style="color: rgb(128, 128, 128);">></span><span class="colour" style="color: rgb(212, 212, 212);">Flask Blog</span><span class="colour" style="color: rgb(128, 128, 128);"></</span><span class="colour" style="color: rgb(86, 156, 214);">title</span><span class="colour" style="color: rgb(128, 128, 128);">></span>
<span class="colour" style="color: rgb(212, 212, 212);">{% </span><span class="colour" style="color: rgb(86, 156, 214);">endif</span><span class="colour" style="color: rgb(212, 212, 212);"> %}</span>

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

<span class="colour" style="color: rgb(86, 156, 214);">from</span><span class="colour" style="color: rgb(212, 212, 212);"> flask </span><span class="colour" style="color: rgb(86, 156, 214);">import</span><span class="colour" style="color: rgb(212, 212, 212);"> Flask, render\_template, url\_for</span>

<link rel='stylesheet' href="{{ url\_for('static'), filename='main.css'}}">

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
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
