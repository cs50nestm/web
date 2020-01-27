# First Flask App

## tl;dr
Build a simple flask app to gain an understanding of how to use this framework.

## Getting Ready

<style type="text/css">
.iframe_container {
	position: relative;
	padding-bottom: 56.25%; 
	padding-top: 25px;
	height: 0;
	margin-bottom: 30px;
}

.iframe_container iframe {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
}
</style>

First watch this video with Brian Yu to deepen your understanding of how Flask works:

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/GhB6Q7KC-SM?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

## Hello, Flask
Create a new folder named, `hello` in your IDE. In this folder, create a simple flask app that creates an html page and says hello, as we did in class. Create a new file in this folder named `application.py` just as Brian does and type in the following:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index:
    return "Hello, World!"
```    

To run your app, type “flask run” into the terminal, and you will get a link to click, similar to when you run http-server.

You’ve written a Flask app!  The most mysterious line in the app you’ve written is probably the one where you wrote:

```python
@app.route("/")
```

This kind of function is called a decorator. [You can read more about decorators here](https://realpython.com/primer-on-python-decorators/) if you want, or you can just keep using them for now.

This line tells Flask that if an http request comes in for “/”, the index function should be run.  The index() function returns a little snippet of html, which could be a whole html page but isn’t here for brevity.

## Templates
Instead of putting html code right in our python program, we can move our html into separate files. Since an app will likely include a number of similar html files, we can create one `layout.html` file that all our html files use. Inside the `hello` folder, make two folders, called `templates`, and `static`. All your html files will go in the `templates` folder.  Your style sheet will go in the `static` folder.

We need a way to execute code and insert variables into our html files, and Flask gives us a way. The name for this is [Jinja](https://palletsprojects.com/p/jinja/), which is a template engine for Python.

Using Jinja, our layout.html file looks like this:

```html
<!DOCTYPE html>

<html lang="en">
  <head>
    <link href="/static/styles.css" rel="stylesheet">
    <title>Hello, Flask</title>	  
  </head>
  <body>
    <h1>Hello, Flask</h1>
    <div class="main">
      {% block main %}{% endblock %}
    </div>
  </body>
</html>
```
