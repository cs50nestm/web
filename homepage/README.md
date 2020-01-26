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

# Problem: Homepage

## tl;dr
Build a simple website of your **Landmark Essay** using HTML and CSS in the [CS50 IDE](https://ide.cs50.io).

## Background
The internet has enabled incredible things: we can use a search engine to research anything imaginable, communicate with friends and family members around the globe, play games, take courses, and so much more. But it turns out that nearly all pages we may visit are built on three core languages, each of which serves a slightly different purpose:

1. HTML, or HyperText Markup Language, which is used to describe the content of websites;
2. CSS, Cascading Style Sheets, which is used to describe the aesthetics of websites; and
3. JavaScript, which is used to make websites interactive and dynamic.

Focusing on just the first two of those three languages for now, create a simple website consisting of four html pages using text and images from your Landmark Essay. 

## Getting Ready

First watch this video with Brian Yu on using `HTML` in the CS50 IDE:

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/78wdlyzrKOA?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allowfullscreen="allowfullscreen"> </iframe>
</div>


Then watch Brian add `CSS` to his webpage:


<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/g7nZFp2zSJ4?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allowfullscreen="allowfullscreen"> </iframe>
</div>


## Getting Started
Here’s how to download this problem’s "distribution code" (i.e., starter code) into your own CS50 IDE. Log into [CS50 IDE](https://ide.cs50.io) and then, in a terminal window, execute each of the below.

1. Execute `cd` to ensure that you’re in` ~/` (i.e., your home directory, aka ~).
2. Execute `mkdir chapter5 to make (i.e., create) a directory called `chapter5` in your home directory.

Execute `cd chapter5` to change into (i.e., open) that directory.

Execute `wget http://cdn.cs50.net/ap/2019/problems/homepage/homepage.zip` to download a (compressed) ZIP file with this problem’s distribution.

Execute `unzip homepage.zip` to uncompress that file.

Execute `rm homepage.zip` followed by `yes` or `y` to delete that ZIP file.

Execute `ls`. You should see a directory called `homepage`, which was inside of that ZIP file.

Execute `cd homepage` to change into that directory.

Execute `ls`. You should see this problem’s distribution code, including `index.html` and `styles.css`.

You can immediately start a server to view the site by typing

```
http-server
```

in the terminal window and clicking on the link that appears, which should be of the form `https://UNIQUEID-ide.cs50.xyz:8080`, where `UNIQUEID` is a long, alphanumeric slug specific to your account.

## Specification
Implement in your `homepage` directory a website that must:

Contain at least four different `.html` pages, at least one of which is `index.html` (the main page of your website), and it should be possible to get from any page on your website to any other page by following one or more hyperlinks.

Use at least ten (10) distinct HTML tags besides `<html>`, `<head>`, `<body>`, and `<title>`. Using some tag (e.g., `<p>`) multiple times still counts as just one (1) of those ten!

Integrate one or more features from Bootstrap into your site. Bootstrap is a popular library (that comes with lots of CSS classes and more) via which you can beautify your site. See Bootstrap’s documentation to get started. To add Bootstrap to your site, it suffices to include

```html
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet">
```

in your pages' <head>, below which can

```html
<link href="styles.css" rel="stylesheet">
```

containing your own CSS.

* Have at least one stylesheet file of your own creation, `styles.css`, which uses at least five (5) different CSS selectors (e.g. tag (example), class (`.example`), or ID (`#example`)), and within which you use a total of at least five (5) different CSS properties, such as `font-size`, or `margin`; and
* Ensure that your site looks nice on browsers both on mobile devices as well as laptops and desktops.
* No need to include any JavaScript on your site for this problem set, unless so inclined!

## Testing
If you want to view how your site looks while you work on it, there are two options:

Within CS50 IDE, navigate to your `homepage` directory (remember how?) and then execute

```
$ http-server
```

1. Within CS50 IDE, right-click (or Ctrl+click, on a Mac) on the `homepage` directory in the file tree at left. From the options that appear, select **Serve**, which should open a new tab in your browser (it may take a second or two) with your site therein.

Recall also that by opening Developer Tools in Google Chrome, you can simulate visiting your page on a mobile device by clicking the phone-shaped icon to the left of Elements in the developer tools window, or, once the Developer Tools tab has already been opened, by typing Ctrl+Shift+M on a PC or Cmd+Shift+M on a Mac, rather than needing to visit your site on a mobile device separately!

## Hints
For fairly comprehensive guides on the languages introduced in this problem, check out the documentation for each on W3Schools.

* [HTML](https://www.w3schools.com/html/)

* [CSS](https://www.w3schools.com/css/)

## Assessment
No `check50` for this assignment! Instead, your site’s correctness will be assessed based on whether you meet the requirements of the specification as outlined above, and whether your HTML is well-formed and valid. 

Consider also:

* whether the aesthetics of your site are such that it is intuitive and straightforward for a user to navigate;
* whether your CSS has been factored out into a separate CSS file(s); and
* whether you have avoided repetition and redundancy by “cascading” style properties from parent tags.

Afraid `style50` does not support HTML files, and so it is incumbent upon you to indent and align your HTML tags cleanly. Know also that you can create an HTML comment with:

```html
<!-- Comment goes here -->
```

but commenting your HTML code is not as imperative as it is when commenting code in, say, C or Python. You can also comment your CSS, in CSS files, with:

```css
/* Comment goes here */
```

## How to Submit
### Step 1 of 2

Ensure that index.html is in ~/chapter5/homepage, as with:

```
cd ~/chapter5/homepage
ls
```

If index.html is not in ~/chapter5/homepage, move it into that directory, as via mv (or via CS50 IDE’s lefthand file browser).

### Step 2 of 2
To submit homepage, execute

```
cd ~/chapter5/homepage
submit50 cs50/problems/2019/ap/homepage
```

inputting your GitHub username and GitHub password as prompted.

Your submission should be graded for completion only within 2 minutes, at which point your score will appear at submit.cs50.io!

This was Homepage.
