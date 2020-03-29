# DVD Animation

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

Ths goal of this lab is to create a DVD animation as seen in this episode of The Office.

<div class="iframe_container">
  <iframe src="https://www.youtube.com/watch?v=QOtuX0jL85Y&t=3s?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>


But first we need to become familiar with drawing with `p5.js`.

{% next %}

## Getting Ready
For this project you will `p5.js`, a JavaScript library that has a full set of drawing and animation tools. Note that in this lab there are separate `HTML` and `JavaScript` files. The `HTML` does nothing more than import the required p5 libararies as well as the JavaScript files you will create so that you can run your animations. You do not need to change the HTML at this point, all your programming will be done in your `sketch.js` file.


A typical `p5.js` sketch starts with a p5 function, `setup()`. Instructions in the `setup()` function are run once when the program starts. It's used to define initial environment properties such as screen size and background color and to load media such as images and fonts as the program starts.

```javascript
function setup() {
  createCanvas(600, 400)
}
```

This will create your `canvas` as a rectangular area on your web page, with a width of 600 and a height of 400.

Another p5 function you will be using is `draw()`. The `draw()` function runs immediately after `setup()`, and it runs repeatedly, allowing for moving animation.  A single execution of the `draw()` function from top to bottom represents a single “frame” of an animation.  The number of times `draw()` executes in each second may be controlled with the `frameRate()` function. The default frame rate is 60 frames per second. There can only be one `draw()` function for each sketch. 

```javascript
function draw() {
  // put your code for drawing here
}
```

{% next %}

Here is a representation of pixels on a 400 x 400 canvas. Note that the y-axis is flipped compared to your math class!

![Canvas](http://intro2018.cs50nestm.net/wp-content/uploads/2019/03/canvas.png)

A few of the p5.js functions you will find useful include:
1. `fill(color)` which sets the color that all subsequent shapes are filled with. For example, `fill(50)` fills shapes with grayscale, while `fill(204, 102, 0)` fills shapes with orange. [p5js.org fill() reference](https://p5js.org/reference/#/p5/fill)
1. `ellipse(x, y, width, height)` draws an ellipse, specifying the coordinates (x,y) of the center, width, and height.  
1. `rect(x, y, width, height)` draws a rectangle, specifying the coordinates (x,y) of the top left corner, width, and height. [Check out `rectMode()` here](https://p5js.org/reference/#/p5/rectMode).
1. `triangle(x1, y1, x2, y2, x3, y3)` draws a triangle, specifying the coordinates of three vertices: (x1,y1), (x2,y2), and (x3,y3)

More functions and details on these functions can be found at [https://p5js.org/reference](https://p5js.org/reference).

{% next %}

## Getting Started
Here’s how to download this problem’s "distribution code" (i.e., starter code) into your own CS50 IDE. Log into [CS50 IDE](https://ide.cs50.io) and then, in a terminal window, execute each of the below.

1. Execute `cd` to ensure that you’re in` ~/` (i.e., your home directory, aka ~).
4. Execute `wget https://intro.cs50nestm.net/wp-content/uploads/2020/03/dvd.zip` to download a (compressed) ZIP file with this problem’s distribution.
5. Execute `unzip dvd.zip` to uncompress that file.
6. Execute `rm dvd.zip` followed by `yes` or `y` to delete that ZIP file.
7. Execute `ls`. You should see a directory called `dvd`, which was inside of that ZIP file.
8. Execute `cd dvd` to change into that directory.
9. Execute `ls`. You should see this problem’s distribution code, including `index.html`, `style.css` and `sketch.js`
10. You can immediately start a server to view the site by typing

```
http-server
```

in the terminal window and clicking on the link that appears.

{% next %}


## Specification

1. Working in the file sketch.js, start by creating a rectangle and have it bounce off the sides of the screen.

1. Have the rectangle change colors when bouncing off the side of a screen (this can be random, or a predetermined set of colors)

1. Load the DVD logo into your sketch and replace the rectangle with this logo: [https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8j2ZvogClZN_eBG7qKeZUCcHweqjjsulAsOGOzKvhkQ2iEEzF](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8j2ZvogClZN_eBG7qKeZUCcHweqjjsulAsOGOzKvhkQ2iEEzF)


### Extension
1. When the rectangle hits a corner of the screen, have it stop the animation and display some sort of celebratory gif or message on the screen.

1. Have rectangle play a “boing” sound when it bounces off the side of a wall.

## Hints

More functions and details on these functions can be found at [https://p5js.org/reference](https://p5js.org/reference).

## How to Submit

Be sure to change directories in your terminal so that the submit50 can access your `sketch.js`, `style.css` and `index.html` files. 

```
cd dvd
```

To make sure you've done this correctly, type `ls` into your terminal, where you should see these two files.

You may then submit by typing in at the command line:

```
submit50 cs50nestm/checks/2019/html
```



