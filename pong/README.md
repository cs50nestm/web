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
<iframe src="https://www.youtube.com/embed/M2XxTDmMZ80" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

#### Part 5 (TODO)
```
5. Use keyPressed() to toggle game state from `start` to `play`.
6. Make ball move when game state is `play`.
7. Bounce ball off top and bottom of canvas.
8. Implement collision checking to bounce ball off of paddle.
```

#### Part 6 (TODO)
```
9.  Implement `serve` game state.
10. Implement scoring.
11. Implement victory.
12. Audio update.
```


## Getting Started
I highly recommend dowloading [Visual Studio](https://visualstudio.microsoft.com/) with [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer&ssr=false#overview) installed on your own computer to develop and test your code.

1. Download this problem’s "distribution code" (i.e., starter code) onto your computer. Copy and paste `https://github.com/cs50nestm/web/raw/master/pong/pong.zip` into the address bar of your web browser to download a (compressed) ZIP file. 
2. Drag this zip file into a folder where you will develop your application, then open that folder in VS Studio.
5. Execute `unzip pong.zip` in the terminal you will have access to in VS Studio.
6. Execute `rm pong.zip` to delete that ZIP file.
7. Execute `ls`. You should see a directory called `pong`.
8. Execute `cd pong` to change into that directory.
9. Execute `ls`. You should see this problem’s distribution code, including `sketch.js`, `index.html` and `style.css`.
12. Your now ready to start working on your game!
13. Follow the Live Server documentation to preview your application.


## Specification

1. Create the game, as per the videos, and add at least one personal feature, to make it your own.

## Rubric

1. **90%** Submit as shown in the class videos
1. **100%** Add one personal touch
