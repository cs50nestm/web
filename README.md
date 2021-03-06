# Pong

The goal of this project is to create Pong, one of the earliest 2-D archade games, originally released by Atari back in 1972. Your job is to recreate Pong 
either on your own, or as a code-a-long with the videos. You may then totally customize it to make it your own.

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

This is a video clip of the original!

<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/fhd7FfGCdCo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
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
2. Create the functions `paddleCollide()`, `countLives()`
3. Create a brick object, and an array of bricks
4. Create the function `dispayBricks()` to iterate through the brick array and draw each to the canvas
```
Video to come!

#### Part 3
```
5. Fill the bricks with different colors for each row
6. Create the `hitBrick()` function which deletes a brick when the ball collides with it
```
Video to come!

#### Part 4
```
7. Make the `gameInit()` and `checkWin()` functions to determine when the game is over and restart the game
8. Create HTML and CSS to style the game as a web page
```
Video to come!

## Getting Started

You can start by copying one of the folders you've used before for a prior p5 project, or download the starter folder as outlined here.

1. Execute `cd` to ensure that you’re in ~/ (i.e., your home directory, aka ~).
2. Execute `wget https://github.com/cs50nestm/web/raw/master/brick_breaker/breakout.zip` to download a (compressed) ZIP file with the p5 starter files.
1. Execute `unzip p5_folder.zip` to uncompress that file.
1. Execute ls. You should see a directory called `p5_folder`, which was inside of that ZIP file.
1. Rename this folder to `brick_breaker`.
1. Execute `cd brick_breaker` to change into that directory.
1. Execute ls. You should see the p5 starter code, including index.html, style.css and sketch.js
1. Feel free to use this p5 starter code for other p5 projects. If you leave the `p5_folder.zip` in your directory, you can unzip it again in the future to start another project.

## Specification

1. Create the game, as per the videos, and add at least one personal feature, to make it your own.

## Rubric

1. **90%** Submit as shown in the class videos
1. **100%** Add one personal touch

## How to Submit

submit50 cs50nestm/checks/2020/brick_breaker
