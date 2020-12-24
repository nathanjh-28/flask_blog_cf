# Flask Outline

Getting Setup
1\. Make project directory and CD in to it\.  Create virtual environment and enter it\.

`python3 -m venv .env`
`source .env/bin/activate`

2\. Install Flask
`% pip install Flask`
3\. Create your entry point python file\, it could be index\.py or server\.py or app\.py
`% touch app.py`

**/app.py**

<span class="colour" style="color:rgb(106, 153, 85)">#\_\_ This imports the module Flask and makes an instance of it called app.</span>
<span class="colour" style="color:rgb(86, 156, 214)">from</span><span class="colour" style="color:rgb(212, 212, 212)"> flask </span><span class="colour" style="color:rgb(86, 156, 214)">import</span><span class="colour" style="color:rgb(212, 212, 212)"> Flask</span>
<span class="colour" style="color:rgb(212, 212, 212)">app = Flask(\_\_name\_\_)</span>

<span class="colour" style="color:rgb(106, 153, 85)">#\_\_ Use decorators for paths and functions to handle the response</span>
<span class="colour" style="color:rgb(212, 212, 212)">@app.route(</span><span class="colour" style="color:rgb(206, 145, 120)">"/"</span><span class="colour" style="color:rgb(212, 212, 212)">)</span>
<span class="colour" style="color:rgb(86, 156, 214)">def</span><span class="colour" style="color:rgb(212, 212, 212)"> hello():</span>
<span class="colour" style="color:rgb(86, 156, 214)">return</span><span class="colour" style="color:rgb(212, 212, 212)"> </span><span class="colour" style="color:rgb(206, 145, 120)">"Hello World!"</span>

4\. Set environment variable in terminal\.  This sets the entry point for the server\.
`% export FLASK_APP=app.py`
Run the server
`% flask run`

5\. Debug Mode
`% export FLASK_DEBUG=1`
This allows your server to refresh on it's own so you don't have to restart your server every time.

<br>
<br>
<br>
<br>
<span class="colour" style="color:rgb(206, 145, 120)"></span>