# Breakout

## tl;dr
Build a Breakout game.

## Preview
Once the game is complete, it could look something like this. You can then customize it to add powerups, varied size paddles, locked bricks and your own creative touches!

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
  <iframe src="https://www.youtube.com/embed/QQm50ZCrEVU?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

## What to Do
This problem will take several steps to complete. The videos below will guide you through this. I will, of course, be available as well to help explain and troubleshoot. After completing this code-a-long, the goal will be to add your own enhancement to the game.

The graphics and the logic for this game were borrowed from [**CS50's Introduction to Game Development**](https://cs50.harvard.edu/games/2018/), which is made available under a [Creative Commons License](https://cs50.harvard.edu/games/2018/license). It uses the programming language Lua and the game framework LÖVE2D, which must be physically installed on a computer. This version is web based and uses JavaScript and p5js.

Topics that this code-a-long will cover include:
* Sprite Sheets
* Procedural Layouts
* Managing States
* Levels
* Player Health
* Particle Systems
* Collision Detection Revisited 
* Persistant Saved Data

#### Part 1 
	1. State flow
	2. Project organization
	3. Distro code
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/Bcb14cQtLZM?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

#### Part 2
	4. Sprite sheets
	5. Generating quads
	6. The paddle class
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/x44u3vYMIlk?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>
	
#### Part 3
	7. The ball class
	8. The bounce update
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/Wkkbfx8Mzqs?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

#### Part 4
	 9. Play State
	10. Ball / Paddle Collision
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/Il6BX2hpxLM?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

#### Part 5
	11. The brick class
	12. Level Maker

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/EI0ZPPPN7Kg?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

#### Part 6
	13. The collision update
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/Ax7tzqlCv00?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>		
	
#### Part 7

	14. Adding health (hearts)
	15. Adding the score
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/e80NeLxxVNQ?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

#### Part 8

	15. Levels and Tiers
	16. Particle Update

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/dJU5fKjNYmU?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

#### Part 9

	17. Victory State
	18. Serve State

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/9oBHEVfheJg?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

#### Part 10
	
	18. Start State
	19. Paddle Select State
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/4KRXldVC3jY?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

#### Part 11

	20. High Scores Update
	
*Note that this is almost an hour long video. Adding the high scores involves multiple steps.*
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/X1Hvcqu08hY?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

#### Part 12
	21. Game Music
	22. Corrections
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/_3yUiQvuuug?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>		
	
	
## Getting Started
I highly recommend working in the new code.cs50.io (VS Code in the Web) development environment.

1. Execute `wget https://github.com/cs50nestm/web/raw/master/breakout2022/breakout.zip` to download a (compressed) ZIP file with this problem’s distribution.
5. Execute `unzip breakout.zip` in the terminal you will have access to in VS Studio.
6. Execute `rm breakout.zip` to delete that ZIP file.
7. Execute `ls`. You should see a directory called `breakout`.
8. Execute `cd breakout` to change into that directory.
9. Execute `ls`. You should see this problem’s distribution code, including `sketch.js`, `index.html` and `style.css`.
12. Your now ready to start working on your game!
13. Execute `http-server` to preview your application.

## Specification

Create the game, as per the videos, and add one personal feature, to make it your own. Here are some ideas on how to take Breakout to the next level!

* Add the ability to pause the game when you press the spacebar.

* Add a Powerup class to the game that spawns a powerup (images located at the bottom of the sprite sheet in the distribution code). This Powerup should spawn randomly, be it on a timer or when the Ball hits a Block enough times, and gradually descend toward the player. Once collided with the Paddle, two more Balls should spawn and behave identically to the original, including all collision and scoring points for the player. Once the player wins and proceeds to the VictoryState for their current level, the Balls should reset so that there is only one active again.

* Grow and shrink the Paddle such that it’s no longer just one fixed size forever. The Paddle could shrink if the player loses a heart (but no smaller of course than the smallest paddle size) and could grow if the player exceeds a certain amount of score (but no larger than the largest Paddle). 

* Add a locked Brick (located in the sprite sheet) to the level spawning, as well as a key powerup (also in the sprite sheet). The locked Brick should not be breakable by the ball normally, unless they of course have the key Powerup! The key Powerup should spawn randomly just like the Ball Powerup and descend toward the bottom of the screen just the same, where the Paddle has the chance to collide with it and pick it up. You’ll need to take a closer look at the LevelMaker class to see how we could implement the locked Brick into the level generation. Not every level needs to have locked Bricks; just include them occasionally! Perhaps make them worth a lot more points as well in order to compel their design. Note that this feature will require changes to several parts of the code, including even splitting up the sprite sheet into Bricks!

* Here is what these enhancements could look like!

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/2Dhn6uvnpJE?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	


## Rubric

1. 90% Submit as demonstrated in code-a-longs
2. 100% Add one personal touch
