# Brick Breaker

The goal of this project is to code a Brick Breaker game, either on your own, or as a code-a-long with the videos. You may totally customize it, to make it your own. You can customize the size of the canvase, the colors, the number of bricks, create powerups, additional levels, or just about anything else you can imagine!

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

The final result could (but does not have to) look something like this:

<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/AQeTDaI3ik8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## What to Do

This problem will take several steps to complete. The videos below will guide you through this. I will, of course, be available as well to help explain and troubleshoot.

#### Part 1
```
1. Create a ball and paddle as JavaScript Objects
2. Create the functions `displayBall()`, `updateBall()`, `checkEdges()`, `displayPaddle()`, `paddleMove()`
```

Note: This video assumes you know something about JavaScript objects and arrays. The [mini-lesson linked here](https://cs50nestm.github.io/web/objects-and-arrays/) explains these concepts.

<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/SyDtIDO-TFk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

#### Part 2
```
3. Create the functions `paddleCollide()`, `countLives()`
4. Create a brick object, and an array of bricks
5. Create the function `dispayBricks()` to iterate through the brick array and draw each to the canvas
```

[View the draft video for Part 2.](https://drive.google.com/file/d/1uXncREqZn4yUBxZyNUtlcG7tOQIkt9-4/view?usp=sharing)

#### Part 3
```
6. Fill the bricks with different colors for each row
7. Create the `hitBrick()` function which deletes a brick when the ball collides with it
```
Video to come!

#### Part 4
```
8. Make the `gameInit()` and `checkWin()` functions to determine when the game is over and restart the game
9. Create HTML and CSS to style the game as a web page
```
Video to come!

## Getting Started

You can start by copying one of the folders you've used before for a prior p5 project, or download the starter folder as outlined here.

1. Execute `cd` to ensure that you’re in ~/ (i.e., your home directory, aka ~).
2. Execute `wget https://github.com/cs50nestm/web/raw/master/brick_breaker/breakout.zip` to download a (compressed) ZIP file with the p5 starter files.
1. Execute `unzip breakout.zip` to uncompress that file.
1. Execute ls. You should see a directory called `breakout`, which was inside of that ZIP file.
1. Execute `cd breakout` to change into that directory.
1. Execute ls. You should see the p5 starter code, including index.html, style.css and sketch.js

## Specification

1. Create the game, as per the videos, and add at least one personal feature, to make it your own.

## Rubric

1. **90%** Submit as shown in the class videos
1. **100%** Add one personal touch

## How to Submit

submit50 cs50nestm/checks/2020/brick_breaker


