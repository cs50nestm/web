# Flappy Bird

## tl;dr
Build a Flappy Bird game.

## Preview
Once the game is complete, it could look something like this. Of course, you are welcome to use your own graphics as well!

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
  <iframe src="https://www.youtube.com/embed/UON_cLR4z8Y?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

## What to Do
This problem will take several steps to complete. The videos below will guide you through this. I will, of course, be available as well to help explain and troubleshoot.

#### Part 1 
	1. Creating the infinite scrolling background.
	2. Creating a parallax effect.

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/OleQ2oFU4Zk?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

#### Part 2
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


*Note: There was a slight bug discovered here, where iterating through the `pipes` array using `for (let pipe of pipes)` actually skips drawing the leftmost pipe after deleting pipe[0]. When we execute `pipes.shift()` the rest of the array moves down an index, and so the pipe that was at index 1, is now at index 0. But the loop ends up skipping the drawing of pipe at index 0 for this next iteration of `draw()`, because it's moving on to index 1. This is noticiple if you look very closely at the left most pipe blinking when the pipe to it's left goes off the screen. The solution is to use a for loop that iterates backwards, so that we never skip drawing that pipe during that iteration. The code snippet below shows what this could look like. It also sets a temporary variable `pipe` to each element in the array so additional code does not have to be changed.*

```js
for (let i = pipes.length - 1; i >= 0; i--) {
    let pipe = pipes[i]
```    
	
	
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

Congratulations! You are all done! See if you can enhance it now and add additional levels!
	
## Getting Started
I highly recommend working in the new [code.cs50.io](https://code.cs50.io) (VS Code in the Web) development environment.

1. Execute `wget https://github.com/cs50nestm/web/raw/master/flappy/flappy.zip` to download a (compressed) ZIP file with this problem’s distribution.
2. Execute `unzip flappy.zip` to uncompress that file.
6. Execute `rm flappy.zip` to delete that ZIP file.
7. Execute `ls`. You should see a directory called `flappy`.
8. Execute `cd flappy` to change into that directory.
9. Execute `ls`. You should see this problem’s distribution code, including `sketch.js`, `index.html` and `style.css`.
12. Your now ready to start working on your game!
13. Execute `http-server` to preview your application.

## Specification

1. Create the game, as per the videos, and add one personal feature, to make it your own.

## Rubric

1. 90% Submit as demonstrated in code-a-longs
2. 100% Add one personal touch

## To submit:

There are two parts to submit `Flappy Bird`.

1. Create a short video (screen capture) of your program running, and be sure to include any personal touch you may have implemented. Attach this to the assignment in google classroom.
2. Make sure to `cd` into your `flappy` folder and execute the following in your terminal:

```
submit50 cs50nestm/checks/2025/flappy
```

