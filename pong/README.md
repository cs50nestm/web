# Pong

The goal of this project is to create Pong, one of the earliest 2-D arcade games, originally released by Atari back in 1972. Your job is to recreate Pong 
either on your own, or as a code-a-long with the videos. You may then totally customize it, adding your own personal touches!

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
1. Review the distribution code
2. Create the puck and two paddles
3. Create functions to move the ball and bounce the ball off the top and bottom of the canvas
4. Check if the ball goes past the paddles, and award a point when it does
5. Create the functions to move the paddles, making sure the paddles stay on the canvas
```
<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/M2XxTDmMZ80" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

#### Part 2

The next thing you need to do is create a collision function to check if the ball hits the paddle. Let's try out this AABB collision algorithm which checks the bounding boxes of two objects, to make sure the four sets of opposite sides don't touch or overlap.

This is an example of what your collision function could look like. You would give it two parameters, the x and y coordinates of the left paddle when you want to check for a left paddle hit, and the x and y coordinates of the right paddle when you want to check for a right paddle hit.

Read through this code to see if you can understand how this function works, and then try to implement it in your pong game.

```javascript
function collides(paddleX, paddleY) {
  let puckLeft = x - d/2
  let puckRight = x + d/2
  let puckBottom = y + d/2
  let puckTop = y - d/2

  if (puckLeft >= paddleX + padW/2) {
    return false
  }

  if (puckRight <= paddleX - padW/2) {
    return false
  }

  if (puckTop >= paddleY + padH/2) {
    return false
  }

  if (puckBottom <= paddleY - padH/2) {
    return false
  }

  return true
}
```

You can then call this function from your draw function with arguments 'lPadX, lPadY' to check for a left ball-paddle collision, and with 'rPadX, rPadY' to check for a right ball-paddle collision.

The code could look something like:

```javascript
if (collides(lPadX, lPadY) {
    // add code to make ball bounce off of left paddle
}
else if (collides(rPadX, rPadY) {
    // add code to make ball bounce off of right paddle
}
```

## Getting Started

You can start by copying one of the folders you've used before for a prior p5 project, or download the starter folder as outlined here.

1. Execute `cd` to ensure that you’re in ~/ (i.e., your home directory, aka ~).
2. Execute `wget https://github.com/cs50nestm/web/raw/master/pong/pong.zip` to download a (compressed) ZIP file with the p5 starter files.
1. Execute `unzip pong.zip` to uncompress that file.
1. Execute ls. You should see a directory called `pong`, which was inside of that ZIP file.
1. Execute `cd pong` to change into that directory.
1. Execute ls. You should see the p5 starter code, including index.html, style.css and sketch.js

## Specification

1. Create the game, as per the videos, and add at least one personal feature, to make it your own.

## Rubric

1. **90%** Submit as shown in the class videos
1. **100%** Add one personal touch

## How to Submit

submit50 cs50nestm/checks/2020/pong
