# Plurality (Python)

Implement a program that runs a plurality election, per the below.

```
$ python plurality Alice Bob Charlie
Number of voters: 4
Vote: Alice
Vote: Bob
Vote: Charlie
Vote: Alice
Alice
```

## Background

Elections come in all shapes and sizes. In the UK, the Prime Minister is officially appointed by the monarch, who generally chooses the leader of the political party that wins the most seats in the House of Commons. The United States uses a multi-step Electoral College process where citizens vote on how each state should allocate Electors who then elect the President.

Perhaps the simplest way to hold an election, though, is via a method commonly known as the “plurality vote” (also known as “first-past-the-post” or “winner take all”). In the plurality vote, every voter gets to vote for one candidate. At the end of the election, whichever candidate has the greatest number of votes is declared the winner of the election.


## Getting Started

Here’s how to download this problem’s “distribution code” (i.e., starter code) into your own CS50 IDE. Log into [CS50 IDE](https://ide.cs50.io)  and then, in a terminal window, execute each of the below.

* Execute `cd` to ensure that you’re in `~/` (i.e., your home directory).
* Execute `mkdir unit2` to make (i.e., create) a directory called unit2 in your home directory.
* Execute `cd unit2` to change into (i.e., open) that directory.
* Execute `mkdir plurality` to make (i.e., create) a directory called `plurality` in your `unit2` directory.
* Execute `cd plurality` to change into (i.e., open) that directory.
* Execute `wget https://cdn.cs50.net/2020/fall/psets/3/plurality/plurality.c` to download this problem’s distribution code.
* Execute ls. You should see this problem’s distribution code, in a file called plurality.py.

## Understanding

Let’s now take a look at `plurality.py` and read through the distribution code that’s been provided to you.

The line `MAX = 9` mean that `MAX` is to be treated as a constant (equal to 9) that can be used throughout the program. Here, it represents the maximum number of candidates an election can have.

We then have `candidates = {}`. This defines a new python dict, named candidates, which will keep track of candidate's names and number of votes. Each `key: value` pair represents candidates's `{"name" : votes}`.

Now, take a look at the `main` function itself. See if you can find where the program copies command-line arguments into the `candidates` dictionary, and asks the user to type in the number of voters. Then, the program lets every voter type in a vote (see how?), calling the `vote` function on each candidate voted for. Finally, main makes a call to the `print_winner` function to print out the winner (or winners) of the election.

If you look further down in the file, though, you’ll notice that the `vote` and `print_winner` functions have been left blank. This part is up to you to complete!

## Specification

Complete the implementation of `plurality.py` in such a way that the program simulates a plurality vote election.

* Complete the `vote` function.
	* `vote` takes two arguments, `candidates`, the candidates dict, and `candidate`, representing the name of the candidate who was voted for.
	* If there is a candidate with this name, update that candidate’s vote total to account for the new vote. The `vote` function in this case should return `True` to indicate a successful ballot.
	* If `candidate` does not match the name of any of the candidates in the election, no vote totals should change, and the vote function should return `False` to indicate an invalid ballot.
	* You may assume that no two candidates will have the same name.
	
* Complete the `print_winner` function.
	* The function should print out the name of the candidate who received the most votes in the election, and then print a newline.
	* It is possible that the election could end in a tie if multiple candidates each have the maximum number of votes. In that case, you should output the names of each of the winning candidates, each on a separate line.

You should not modify anything else in `plurality.py` other than the implementations of the `vote` and `print_winner` functions (and the inclusion of additional modules, if you’d like).

## Usage

Your program should behave per the examples below.




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
4. Execute `wget http://cdn.cs50.net/ap/2019/problems/homepage/homepage.zip` to download a (compressed) ZIP file with this problem’s distribution.
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
