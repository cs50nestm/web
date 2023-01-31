# Problem: HTML

## Getting Ready

Beyond introducing you to web programming, the overarching goal of this problem is to empower you to teach yourself new languages so that you can stand on your own at the end of the year. We’ll guide you through each, but if you nonetheless find yourself Googling and asking lots of questions of classmates and staff, rest assured you’re doing it right!

First consider joining Daven for a tour of `HTML`. Focus for now on the `HTML`. We'll add in `CSS` later on.

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

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/dM5V1epAbSs?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>


# What do I do now?

The code you created with your teacher, probably looks something like this, although she probably added a few more features:

```html
<!DOCTYPE html>

<html>
  <head>
    <title>My First Webpage</title>
  </head>
  <body>
    My First Webpage
  </body>
</html>
```

Working in your [codespace](https://code.cs50.io) you will start by typing this code into a file called `index.html`. But first create your directories.

If you haven't yet created a new directory for this unit, create one called `unit3` or whatever you prefer, then `cd` into it.

```
mkdir unit3
cd unit3
```

When working on web based programs, it's important to have a separate directory for each project. So create a new directory, `cd` into it, then make your html file and name it `index.html`.

```
mkdir html
cd html
code index.html
```

Then to start up a server to be able to view your web page, type:

```
http-server
```

into the terminal window, and then click on provided link. You will see a directory of all files in your current directory. Then click on the `mypage.html` link and you can preview your page.

Once `http-server` is running, you can preview any changes just by clicking on the refresh button.

So let's go about customizing this web page to make it all about you!

**First**, let's add a heading to the top of your page.
 
Right under the first `<body>` tag, add an open and close `<h1>` tag with your name as follows:

```html
<h1>Margaret Tanzosh</h1>
```

With your name instead of mine!

**Second**, add a picture of yourself, or something you like using `<img>` tags.

If you find a picture of yourself online, or email one to yourself, you can drag the '.jpg' or '.png' file into your workspace. Make sure the name of the file has no spaces in it. If I had a picture saved as a `mtanzosh.png` in my workspace (click on the directory sidebar foler icon to the left of the `mypage.html` tab to see the files in your workspace), I could then import it as

```html
<img alt="Tanzosh" src="mtanzosh.png">
```                                    

**Third**, add a paragraph about yourself, under the `<img>` tag using paragraph tags:

```html
<p>This is information about me!</p>
```

**Fourth**, add a link to your favorite website, using an anchor tag:

```html
<a href="https://www.google.com">A website I use all the time!</a>
```

And change the text in between the `<title></title>` tags and notice what happens to your Chrome (or other browser) tab on the top of your page!

Once you understand the structure of an `HTML` page, you can look up the many kinds of `HTML` tags to add other elements to your page as well. Feel free to experiment in this lab. Use the [W3 Schools reference](https://www.w3schools.com/html/) to get ideas on other elements for your page.

Do notice how tags inside of tags are indented. As when working in C, proper indentation makes your page much easier to read.

Because this assignment will result in something different for each person, there’s no check50 for this one. There is also no style50 for HTML, so check the indendentation yourself. Make sure that you’ve included everything listed above and you have no broken links and you should be good to go.

## How to View Your Web Page

Type `http-server` in the terminal and then refresh the browser tab!

## To get more help with HTML

* [HTML](https://www.w3schools.com/html/)

## How to Submit

Make sure you first `cd` into the diretory that contains your `html` file. You may then submit by typing in at the command line:

```
submit50 cs50nestm/checks/2020/html
```

<!--

# Problem: Temperature Conversion

## tl;dr
Complete the JavaScript code to add funcionality to a temperature conversion web page in the [CS50 IDE](https://ide.cs50.io).

![thermometer](https://i.ytimg.com/vi/CHn_lLbnm8c/maxresdefault.jpg)


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

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/WzfPjOYmjxg?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

## Getting Started
Here’s how to download this problem’s "distribution code" (i.e., starter code) into your own CS50 IDE. Log into [CS50 IDE](https://ide.cs50.io) and then, in a terminal window, execute each of the below.

1. Execute `wget https://intro.cs50nestm.net/wp-content/uploads/2020/02/temperature.zip` to download a (compressed) ZIP file with this problem’s distribution.
2. Execute `unzip temperature.zip` to uncompress that file.
3. Execute `rm temperature.zip` followed by `yes` or `y` to delete that ZIP file.
4. Execute `ls`. You should see a directory called `temperature`, which was inside of that ZIP file.
5. Execute `cd temperature` to change into that directory.
6. Execute `ls`. You should see this problem’s distribution code, including `index.html` and `styles.css`.
7. You can immediately start a server to view the site by typing

```
http-server
```

in the terminal window and clicking on the link that appears.

## Specification

This program uses HTML, CSS and JavaScript to create a temperature conversion web page, where you will convert Celsius to Fahrenheit and Fahrenheit to Celsius.

The HTML and CSS is already written for you, though you are welcome to customize it. Your challenge will be to write the JavaScript to make the program functional.

In between the

```html
<script>
</script>
```

tags, you will write JavaScript to access the value enterred into the text box, and depending on whether the user chooses `fahrenheit to celsius` or `celsius to fahrenheit` you will calculate the appropriate value and add it to the `div` with `id="result"` in `index.html`.

When the button is clicked, html will call the `convert()` function that you will write. 

## How to Start

You may want to create some shortcuts to be able to access the input value, the select value and the output area from your HTML. You can do this by creating three variables as follows:

```javascript
let input = document.querySelector("#tempInput")
let choice = document.querySelector("#choose")
let output = document.querySelector("#result")
```

Once the user enters a number in the text box, you can access the value with `input.value`. In the same way, you can access the value of the conversion choice with `choice.value`. Finally, you can add your own text to the `result` div by assigning the desired string to `output.innerHTML`.

Now write the function convert(). You can start this as:

```javascript
function convert() {
  // TODO

}
```

Remember this function will execute when the user clicks the `convert` button, so this would be a good time to get the number of degrees entered, the choice the user makes for conversion and test that these values are not blank. If either of these values is missing (when the choice is missing choice.value will be equal to "none") use a JavaScript alert to yell at the user and return from this function.

Now you can test if choice.value is equal to "ftoc" in which case you will want to calculate degrees celsius, or "ctof" in which you will want to calculate degrees fahrenheit. 

After performing the appropriate calculation, create a string using JavaScript concatenation that says something like:

```
100 degrees fahrenheit is 37.8 degrees celsius
```

Finally make sure your output uses exactly one decimal point for ease of reading.

## Hints

For fairly comprehensive guides on the languages introduced in this problem, check out the documentation for each on W3Schools.

* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css)
* [JavaScript](https://www.w3schools.com/js)

## How to Submit


```submit50 cs50nestm/checks/2019/temperature
```

-->
