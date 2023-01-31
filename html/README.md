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
submit50 cs50nestm/checks/2022/html
```


