# Mario

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
This problem will take several steps to complete. The videos below will guide you through this. I will, of course, be available as well to help explain and troubleshoot.

#### Part 1 
	1. Creating the `generateTiles()` function
	2. Creating the `Sprite` class
	3. Creating the game map using a csv file

Note: This video assumes you know something about JavaScript objects and arrays. The [mini-lesson linked here](https://cs50nestm.github.io/web/objects-and-arrays/) explains these concepts.

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/NsnyzDOsttI?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>
	
#### Part 2
	4. Creating the alien player sprite
	5. Preparing to animate the alien sprite
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/AJlrXMHs1Oc?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

#### Part 3
	6. Animating and controling the alien sprite
	7. Collision checking

<!-- Part 2b: [Unedited Video for Mario 2b](https://drive.google.com/drive/u/0/folders/0BxQd8HnFed5OflRmVmNMZ2pQQzFiNkxUY0hiczFvMS1WUllmV0hjT1ltdDA4V3g3M09TMHM) -->

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/PM19RF5uEoE?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

#### Up for a challenge?
Can you add a direction property to the Animated Sprite class so that your alien turns left when walking to the left? You might find the p5 functions `push()`, `scale()` and `pop()` come in helpful.

Also if you finish early, why not start creating the first level of your game world by customizing your tile map!

#### Part 4
	7.  Adding gravity
	8.  Resolving platform collisions
	9.  Adding scrolling
	
*Note: In the video there is a section when creating the function `resolvingPlatformCollisions` that I seem to have a problem with the line `s.y = 0`, but when I tested this out this week, it seemed to work fine.*

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/QtKfO3xjPoQ?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

#### Part 5
	10. Adding `checkDeath()` and `checkGameOver()` functions
	11. Adding sound effects
	
*Note: After adding the Game Over text, you'll notice that the coins and lives no longer line up properly. That was because I centered the text in `checkGameOver()` but forgot to left align the text in `displayScore()`.*
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/asXG5fe5cZM?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

#### Part 6
	12. Miscellaneous fixes
	
<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/BHuJdLlEYUk?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

#### Part 7
	13. Adding enemies
	
]<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/7_CV96ndyc4?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>	

And now go ahead and customize your game map for a fully completed game!

For inspiration, [check out the project students completed last year!](https://beelee115.github.io/BlueMan%20Descends%20to%20Madness/index.html)

<!-- Part 3: [Unedited Video for Mario 3](https://drive.google.com/drive/u/0/folders/0BxQd8HnFed5OflRmVmNMZ2pQQzFiNkxUY0hiczFvMS1WUllmV0hjT1ltdDA4V3g3M09TMHM)

Part 3b: [Unedited Video for Mario 3b](https://drive.google.com/file/d/1yASqexKXDWfEaTv6i8PhnSB6s-yl5cV2/view?usp=sharing)

Part 3c: [Fixing Glitches](https://drive.google.com/file/d/1thahTK9CQp6pI356WeDaTBNrYexmQVyA/view)

 -->
## Getting Started
I highly recommend dowloading [Visual Studio](https://visualstudio.microsoft.com/) with [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer&ssr=false#overview) installed on your own computer to develop and test your code.

1. Download this problem’s "distribution code" (i.e., starter code) onto your computer. Copy and paste `https://github.com/cs50nestm/web/raw/master/mario/mario.zip` into the address bar of your web browser to download a (compressed) ZIP file. 
2. Drag this zip file into a folder where you will develop your application, then open that folder in VS Studio.
5. Execute `unzip mario.zip` in the terminal you will have access to in VS Studio.
6. Execute `rm mario.zip` to delete that ZIP file.
7. Execute `ls`. You should see a directory called `mario`.
8. Execute `cd mario` to change into that directory.
9. Execute `ls`. You should see this problem’s distribution code, including `sketch.js`, `index.html` and `style.css`.
10. You can find additional graphics for customizing your game later, [here](https://github.com/games50/mario/tree/master/mario/graphics).
12. Your now ready to start working on your game!
13. Follow the Live Server documentation to preview your application.

## Specification

1. Create the game, as per the videos, and add one personal feature, to make it your own.

## Rubric

1. 90% Submit as demonstrated in code-a-longs
2. 100% Add one personal touch


<!-- ## How to Submit

submit50 cs50nestm/checks/2020/mario -->
