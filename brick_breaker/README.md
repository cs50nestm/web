# Brick Breaker

The goal of this project is to code along with the live class (or videos) and add one personal touch, to make it your own. This could be changing the colors, changing the number of bricks, or something else.

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

The final result shoud look something like this:

<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/UvXiMSsKpbs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Using p5.js, we started in a similar way as the paddle and ball game we created a few weeks back. Our canvas is vertical, with a width of 400 and a height of 600, and we added an array of brick objects on top of the screen. We then added a function to iterate thorugh this array of bricks to determine if the ball hits one of the bricks. When we get a ball-brick collision we remove the brick from the array of bricks and increase the score.

Finally, we added a game initialization function, that restarts the game by resetting the number of lives and the score and restores all the bricks.

## Getting Started

You can start by copying one of the folders you've used before for a prior p5 project, or download the starter folder as outlined here.

1. Execute `cd` to ensure that you’re in ~/ (i.e., your home directory, aka ~).
2. Execute `wget https://github.com/cs50nestm/web/raw/master/brick_breaker/p5_folder.zip` to download a (compressed) ZIP file with the p5 starter files.
1. Execute `unzip p5_folder.zip` to uncompress that file.
1. Execute ls. You should see a directory called `p5_folder`, which was inside of that ZIP file.
1. Rename this folder to `brick_breaker`.
1. Execute `cd brick_breaker` to change into that directory.
1. Execute ls. You should see the p5 starter code, including index.html, style.css and sketch.js
1. Feel free to use this p5 starter code for other p5 projects. If you leave the `p5_folder.zip` in your directory, you can unzip it again in the future to start another project.

## Next Step

If you didn't join the live classes where we developed brick breaker together, watch the videos on the Google Classroom site.

## Specification

1. Create the game, as per the videos, and add one personal feature, to make it your own.

## Rubric

1. **90%** Submit as shown in the class videos
1. **100%** Add one personal touch

## How to Submit

submit50 cs50nestm/checks/2019/brickbreaker


