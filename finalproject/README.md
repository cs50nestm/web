# Comp Sci Final Project 2021

## tl;dr
Create a game, a website, an infographic or a presentation.

## Background
The climax of this course is its final project. The final project is your opportunity to take your newfound savvy with programming out for a spin and use it to develop something really special.
For those who prefer learning more about current issues in computing, the option exists to research and create a presentation on a select topic as well. You may work alone, or in a breakout room with teams of up to four members.

## Choices
Here are the four different directions you can choose from:

1. Game or Interactive Animation in p5.js
  	- **[Pong](https://intro.cs50nestm.net/pong/)** (continuing to build on the algorithms logic we developed for the paddle ball project)
  	- **[Brick Breaker](http://intro.cs50nestm.net/brick_breaker/)** (begin to use JavaScript objects and classes, arrays of objects, and integrate into HTML page)
  	- **[Mario](https://intro.cs50nestm.net/mario)** (program the game mechanics as a code-a-long and develop your own game landscape using totally customized tile maps)
  	- **[Flappy Bird, Snake or Space Invaders](https://thecodingtrain.com/CodingChallenges/115-snake-game-redux.html)** using Dan Shiffman's tutorials.

2. **Website** either as a inter-disciplinary project, or on an topic you are particularly passionate about and that helps make the world a better place.
3. Webpage with **[JavaScript infographics](https://intro.cs50nestm.net/virus)**, such as an interactive graphs or charts.
4. Google Slides presenstation on one of the following **impacts of computing**
	- **Beneficial and Harmful Effects:** While computing innovations are typically designed to achieve a specific purpose, they may have unintended consequences.
	- **Digital Divide:** The “digital divide” refers to differing access to computing devices and the Internet, based on socioeconomic, geographic, or demographic characteristics and raises issues of equity, access, and influence.
	- **Computing Bias:** Computing innovations can reflect existing human biases because of biases written into the algorithms or biases in the data used by the innovation.
	- **Crowdsourcing:** Crowdsourcing offers new models for collaboration, such as connecting businesses or social causes with funding.
	- **Legal and Ethical Concerns:** Ease of access and distribution of digitized information raises intellectual property concerns regarding ownership, value, and use.
	- **Safe Computing:** The use of computing innovations may involve risks to personal safety and identity. This may involve risks to privacy and/or unauthorized access to computing resources.


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


## Getting Started
Here’s how to download this problem’s "distribution code" (i.e., starter code) into your own CS50 IDE. Log into [CS50 IDE](https://ide.cs50.io) and then, in a terminal window, execute each of the below.

1. Execute `cd` to ensure that you’re in` ~/` (i.e., your home directory, aka ~).
2. Execute `mkdir chapter5 to make (i.e., create) a directory called `chapter5` in your home directory.
3. Execute `cd chapter5` to change into (i.e., open) that directory.
4. Execute `wget http://cdn.cs50.net/2020/fall/psets/8/homepage/homepage.zip` to download a (compressed) ZIP file with this problem’s distribution.
5. Execute `unzip homepage.zip` to uncompress that file.
6. Execute `rm homepage.zip` followed by `yes` or `y` to delete that ZIP file.
7. Execute `ls`. You should see a directory called `homepage`, which was inside of that ZIP file.
8. Execute `cd homepage` to change into that directory.
9. Execute `ls`. You should see this problem’s distribution code, including `index.html` and `styles.css`.
10. You can immediately start a server to view the site by typing

```
http-server
```

in the terminal window and clicking on the link that appears.

## Specification
Implement in your `homepage` directory a website that must:

Contain at least four different `.html` pages, at least one of which is `index.html` (the main page of your website), and it should be possible to get from any page on your website to any other page by following one or more hyperlinks.

Use at least ten (10) distinct HTML tags besides `<html>`, `<head>`, `<body>`, and `<title>`. Using some tag (e.g., `<p>`) multiple times still counts as just one (1) of those ten!

Integrate one or more features from Bootstrap into your site. Bootstrap is a popular library (that comes with lots of CSS classes and more) via which you can beautify your site. See [Bootstrap’s documentation](https://getbootstrap.com/docs/4.5/getting-started/introduction/) to get started. To add Bootstrap to your site, it suffices to include

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
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
