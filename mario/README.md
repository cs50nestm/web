# Problem: Mario

## tl;dr
Build a Super Mario type platformer game.

## Preview
Once the game is complete, it could look something like this. The game map is totally customizable and yours will most likely look quite a bit different.



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
  <iframe src="https://www.youtube.com/embed/Gc49f1bskUA?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

## What to Do
This problem will take several steps to complete, which we will do together during live and recorded classes. The process wil be:

#### Part 1 
	1. Creating the `generateTiles()` function
	2. Creating the `Sprite` class
	3. Creating the game map using a csv file
	
#### Part 2
	4. Creating the alien player sprite
	5. Animating and controling the alien sprite
	6. Addition gravity and collision checking
	
#### Part 3
	7. Adding jumping
	8. Adding scrolling
	9. Finishing touches: adding score and sound effects


## Getting Started
Here’s how to download this problem’s "distribution code" (i.e., starter code) into your own CS50 IDE. Log into [CS50 IDE](https://ide.cs50.io) and then, in a terminal window, execute each of the below.

1. Execute `cd` to ensure that you’re in` ~/` (i.e., your home directory, aka ~).
4. Execute `wget https://github.com/cs50nestm/web/raw/master/mario/mario.zip` to download a (compressed) ZIP file with this problem’s distribution.
5. Execute `unzip mario.zip` to uncompress that file.
6. Execute `rm mario.zip` followed by `yes` or `y` to delete that ZIP file.
7. Execute `ls`. You should see a directory called `mario`, which was inside of that ZIP file.
8. Execute `cd mario` to change into that directory.
9. Execute `ls`. You should see this problem’s distribution code, including `sketch.js`, `index.html` and `styles.css`.
10. You can immediately start a server to view the site by typing

```
http-server
```

in the terminal window and clicking on the link that appears.

## Specification

1. Create the game, as per the videos, and add one personal feature, to make it your own.

## Rubric

1. 90% Submit as shown in the class videos
2. 100% Add one personal touch


## How to Submit

submit50 cs50nestm/checks/2019/mario
