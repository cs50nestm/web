# Pong

The goal of this project is to create Pong, one of the earliest 2-D arcade games, originally released by Atari back in 1972. We'll start out as a code-a-long, using several game development techniques such as game state. You may then totally customize it, adding your own personal touches!

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

This problem will take several steps to complete. The videos below will guide you through some of this and I will work with you on other parts. I will, of course, be available througout to answer questions and troubleshoot.

#### Part 1
```
1. Review the distribution code and become familiar with p5.js
```

<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/6iWrt7-UUwE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

You can learn more about p5.js by reviewing it's online reference at [p5js.org/](https://p5js.org/)

#### Part 2
```
2. Create the ball class.
```
<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/otMxvYkHUFg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

#### Part 3
```
3. Create the paddle class.
```
<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/aKvTUrqi3Hs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

#### Part 4
```
4. Create the collision algorithm.
```
<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/7OGbz4GeoVk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

#### Part 5
```
5. Use keyPressed() to toggle game state from `start` to `play`.
6. Make ball move when game state is `play`.
```

<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/2xR1MB8kINQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Part 6

```
7. Bounce ball off top and bottom of canvas.
8. Implement `serve` game state.
9. Implement scoring.
```

<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/xaP-kUGLQc8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


#### Part 7

```
10. Write directions to screen
11. Implement victory.
```

<div class="iframe_container">
<iframe src="https://www.youtube.com/embed/lDkPW-vL050" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

#### Part 8
```
12. Audio Update
```
This last part is really simple! First, you'll need to create three global variables for the three sounds, load the sounds, and then play them at the appropriate time.

To start, let's create the global variables which will hold the sounds. At the top of your file, where you declare ball, player1, player2, etc., add the following line of code:

```js
let ponghit, pongbounce, pongscore
```
Then in the `preload()` function, add the following lines to load the three sounds.

```js
ponghit = loadSound("ponghit.wav")
pongbounce = loadSound("pongbounce.wav")
pongscore = loadSound("pongscore.wav")
```

Now, find the parts of your code where your paddle and ball collide. There are two places where this happens. This will be in your `draw()` function. After adjusting the position of `ball.x` (the x coordinate value of the ball) add the following line of code:

```js
ponghit.play()
```
Add the bounce sound when your ball bounces off of the top or bottom of your canvas:

```js
pongbounce.play()
```

Finally, find the two places in your code where the ball goes past the left and right sides of the canvas, giving the opposite player a point. Add the score sound in those two places:

```js
pongscore.play()
```

And that's it! Your game is done!

#### Up for a challenge?

Implement an AI-controlled paddle (either the left or the right will do) such that it will try to deflect the ball at all times. Since the paddle can move on only one axis (the Y axis), you will need to determine how to keep the paddle moving in relation to the ball. Currently, each paddle has its own chunk of code where input is detected by the keyboard; this feels like an excellent place to put the code we need! Once either the left or right paddle (or both, if desired) deflects the ball on its own, you’ve done it!

## Getting Started
I highly recommend working in the new [cs50.dev](https://cs50.dev) (VS Code in the Web) development environment.

2. Execute `wget https://github.com/cs50nestm/web/raw/master/pong/pong.zip` to download a (compressed) ZIP file with this problem’s distribution.
5. Execute `unzip pong.zip` to uncompress that file.
6. Execute `rm pong.zip` to delete that ZIP file.
7. Execute `ls`. You should see a directory called `pong`.
8. Execute `cd pong` to change into that directory.
9. Execute `ls`. You should see this problem’s distribution code, including `sketch.js`, `index.html` and `style.css`.
12. Your now ready to start working on your game!
13. Execute `http-server` to preview your application.


## Specification

1. Create the game, as per the videos, and add at least one personal feature, to make it your own.

## Rubric

1. **90%** Submit as shown in the class videos
1. **100%** Add one personal touch

## To submit:

There are two parts to submit `Pong`.

1. Create a short video (screen capture) of your program running, and be sure to include any personal touch you may have implemented. Attach this to the assignment in google classroom.
2. Make sure to cd into your `pong` folder and execute the following in your terminal:

```
submit50 cs50nestm/checks/2025/pong
```
