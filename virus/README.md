# Virus Simulator

## tl;dr

Build a `p5` animation and integrate with `html` inputs and `chart.js` to simulate the spread of viruses.

## Preview

Once the program is completed, it could look something like this:

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
<iframe src="https://www.youtube.com/embed/_Q0ZAhvEg3E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## What to Do

This program was developed over several live and recorded classes, which you can find on google classroom. My expectation is that you code along with the videos to complete this project, customizing the project as you like.

We started with the distribution code linked below, creating an array of JavaScript objects, 'people' to represent a community. Each people object contains not only x and y properties to determine their location on the canvas, but also a properties related to health. We represent health people with blue dots, sick people with red dots and recovered people with pink dots. Sick people can infect healthy people when they interact, simulated in this case by the dots touching. We finish by connecting code for the chart, which shows how different infection rates may overwhelm hospital capacity.

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

submit50 cs50nestm/checks/2019/brick_breaker


