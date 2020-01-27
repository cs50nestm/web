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

Using Jinja, our `layout.html` file looks like this:

```django
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

The line {% block body %}{% end block %}, is what makes this a layout file.  We can insert whatever code makes up the content of our page in place of this block. A layout file can contain as many blocks as you want. Just give each one a different name.

Now create index.html so that it uses the template, like this:

```django
{% extends "layout.html" %}

{% block body %}
<p>Next we'll put a form here and get some POST action!</p>
{% endblock %}
```

In the static folder, put a style.css file.  I’ve added one style but you can add more.

```css
body {
  background-color: yellow;
}
```

Finally, we’ll go back to `application.py`.  In the initial import, we’ll need a few more functions from Flask.  Then, replace the direct return of html with a call to Flask’s `render_template()` function.

```python
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```

When you run your application now (flask run at the command line), you’ll get a little more out of your app.  But it isn’t really interactive yet.

# Forms

HTML Forms allow the user to enter data into input fields, and send the data to the server using the POST method of the HTTP protocol. [You can learn more about HTML Forms here](https://www.w3schools.com/html/html_forms.asp).

Add a form to index.html so that it looks like this:

```html
{% extends "layout.html" %}

{% block body %}
<form action="/form" method="post">
  What is your name? <br/>
  <input type="text" name="name"><br/>
	
  What is your quest? <br/>
  <input type="radio" name="quest" value="grail">I seek the grail.<br/>
  <input type="radio" name="quest" value="grade">I just want an A.<br/>
  
  What is your favorite color? <br/>
  <select name="color">
    <option value="blue">Blue</option>
    <option value="red">Red</option>
    <option value="oops">Not blue, not red, oops?</option>
  </select>
  <button type="submit">Submit</button>
</form>
{% endblock %}
```

Note that each form element has both a *name* and a *value*. Those are what gets passed into `application.py` for our use when the form is submitted.

Run the program, visit index.html, and submit the form.  You should see the message “Method not allowed”.  So we need to make Flask allow the POST method on `index.html`.

## Post

In `application.py`, we need to add a route to handle the POST request. Here is what our new application.py looks like.
	
```python
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
    
@app.route("/form", methods=["POST"])
def form():
    name = request.form.get("name")
    print(name)
    if request.form.get("quest") == "grail":
        quest = "seek the grail"
    else:
        quest = "join the ratrace"
    color = request.form.get("color")
    if color == "oops":
        return render_template("oops.html", name = name)
    else:
        return render_template("cross.html", name = name, quest = quest)    
```  

This example has some logic in it, using the information provided by the user. The `print()` functions show how you can do a little print debugging, even with Flask. They aren’t necessary for the program to run. The variables *name*, and maybe *quest*, are passed to their templates.  The template `oops.html` looks like this:

```html
{% extends "layout.html %}

{% block body %}
<p>Sorry, {{name}}, you are cast from the bridge to your death. Oops. </p>
{% endblock %}
```

You can see how the value of name is inserted into the HTML.

The template `cross.html` uses both *name* and *quest*.

```html
{% extends "layout.html %}

{% block body %}
<p>Good news, {{name}}, you are allowed to cross the bridge and {{quest}}.</p>
{% endblock %}
```

Try the program now.  If there are any errors, see if you can figure them out by reading the program output on the command line and by using print() statements.

To do a little more, try adding a “Play Again” link to `oops.html` and/or `cross.html`.  

# How to Submit

Execute the code below from your `hello` directory, logging in with your GitHub username and password when prompted.

```
submit50 cs50nestm/checks/2019/flask
```

*Adapted from 27 Classrooms, by Mark Sobkowicz, Lincoln Sudbury Regional High School
*
