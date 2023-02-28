# Hello to JavaScript

## tl;dr
Learn to use JavaScript to get input from a form and use it to modify HTML in your CS50 [codespace](https://code.cs50.io).
<!-- Build a simple website of your **Write My New York** using HTML and CSS in your [codespace](https://code.cs50.io). -->

## Background
JavaScript is often called the "language of the web." It can read input from your webpage and update both HTML and CSS. In this program you will complete the JavaScript portion of distribution code in order to read a name from a text box and use it to update the HTML.

<!-- ## Getting Ready

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

First watch this video with Brian Yu on using `HTML` in the CS50 IDE:

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/78wdlyzrKOA?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>


Then watch Brian add `CSS` to his webpage:


<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/g7nZFp2zSJ4?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allowfullscreen="allowfullscreen"> </iframe>
</div>

Fianally watch the section of the video below, from 1:23 to 7:28 to learn more about how to put the pieces together:


<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/sEVlPyywlfc?start=68&end448=&modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allowfullscreen="allowfullscreen"> </iframe>
</div>
 -->

## Getting Started
Here’s how to download this problem’s "distribution code" (i.e., starter code) into your codespace. Log into [code.cs50.io](https://code.cs50.io) and then, in a terminal window, execute each of the below.

1. Execute `cd` to ensure that you’re in` ~/` (i.e., your home directory, aka ~).
2. Execute `mkdir hellojavascript` to create a new directory.
3. Execute `cd hellojavascript` to move into that directory.
4. Execute `wget https://raw.githubusercontent.com/cs50nestm/web/master/distro/hello.html` to download an html file with this problem’s distribution.
9. Execute `ls`. You should see this problem’s distribution code, `hello.html`.
10. You can immediately start a server to view the site by typing

```
http-server
```

in the terminal window and clicking on the link that appears.

## Specification

In the file `hello.html`, complete the JavaScript to output:

“Hello, world!” when nothing is input into the text box, and “Hello, Margaret” when I entered my name, Margaret as below.

Implement in your `homepage` directory a website that must:

Contain at least four different `.html` pages, at least one of which is `index.html` (the main page of your website), and it should be possible to get from any page on your website to any other page by following one or more hyperlinks.

Use at least ten (10) distinct HTML tags besides `<html>`, `<head>`, `<body>`, and `<title>`. Using some tag (e.g., `<p>`) multiple times still counts as just one (1) of those ten!

Integrate one or more features from Bootstrap into your site. Bootstrap is a popular library (that comes with lots of CSS classes and more) via which you can beautify your site. See [Bootstrap’s documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/) to get started. In particular, you might find some of [Bootstrap’s components](https://getbootstrap.com/docs/5.1/components/accordion/) of interest. To add Bootstrap to your site, it suffices to include

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
```

in your pages' <head>, below which you can also include

```html
<link href="styles.css" rel="stylesheet">
```

containing your own CSS.

* Have at least one stylesheet file of your own creation, `styles.css`, which uses at least five (5) different CSS selectors (e.g. tag (example), class (`.example`), or ID (`#example`)), and within which you use a total of at least five (5) different CSS properties, such as `font-size`, or `margin`; and
* Ensure that your site looks nice on browsers both on mobile devices as well as laptops and desktops.
* No need to include any JavaScript on your site for this problem set, unless so inclined!

## Testing
If you want to view how your site looks while you work on it, there are two options:

Within [code.cs50.io](https://code.cs50.io), navigate to your `homepage` directory (remember how?) and then execute

```
$ http-server
```

1. Within [code.cs50.io](https://code.cs50.io), right-click (or Ctrl+click, on a Mac) on the `homepage` directory in the file tree at left. From the options that appear, select **Serve**, which should open a new tab in your browser (it may take a second or two) with your site therein.

Recall also that by opening Developer Tools in Google Chrome, you can simulate visiting your page on a mobile device by clicking the phone-shaped icon to the left of **Elements** in the developer tools window, or, once the Developer Tools tab has already been opened, by typing `Ctrl`+`Shift`+`M` on a PC or `Cmd`+`Shift`+`M` on a Mac, rather than needing to visit your site on a mobile device separately!

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

Ensure that index.html is in homepage, as with:

```
cd homepage
ls
```

If index.html is not in the homepage directory, move it into that directory, as via mv (or via CS50 IDE’s lefthand file browser).

### Step 2 of 2
To submit homepage, execute

```
cd homepage
submit50 cs50/problems/2022/x/homepage
```

Your submission should be graded for completion only within 2 minutes, at which point your score will appear at submit.cs50.io!

This was Homepage.
