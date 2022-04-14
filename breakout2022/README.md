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

	
<!-- 
### Part 4
	9. The brick update
	
### Part 5
	10. The collision update
	 -->
	

<!-- #### Part 2
	3. Creating the bird class.
	4. Adding gravity
	5. Adding anti-gravity
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/TTfw_ewULdw?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

		
#### Part 3
	6. Creating the pipe class.
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/1Hho76hT48w?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	
	
#### Part 4	
	7. Infinite pipes.
	8. Pairs of pipes.
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/cbgDjru5OGc?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	
	
	
#### Part 5
	9.  Controlling the placement of the pipe gap.
	10. Adding the collision algorithm.
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/TAw4S1ANRvk?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>		
		
#### Part 6	
	11. Using gameState
	12. Adding the title, countdown, play and done gameStates
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/HH2wyDZHVTw?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

#### Part 7
	13. Scoring points
	14. Audio update
	
*Note: In the video the sound doesn't play, but as soon as I stopped recording the sound played perfectly!*	
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/sveIrq06gco?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

Congratulations! You are all done! See if you can enhance it now and add additional levels! -->
	
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

1. Create the game, as per the videos, and add one personal feature, to make it your own.

## Rubric

1. 90% Submit as demonstrated in code-a-longs
2. 100% Add one personal touch
