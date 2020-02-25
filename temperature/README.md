# Problem: Temperature Conversion

## tl;dr
Complete the JavaScript code to add funcionality to a temperature conversion web page in the [CS50 IDE](https://ide.cs50.io).

![thermometer](https://i.ytimg.com/vi/CHn_lLbnm8c/maxresdefault.jpg)

## What is JavaScript?

A simple definition from W3Schools: "JavaScript is the Programming Language for the Web. JavaScript can update and change both HTML and CSS. JavaScript can calculate, manipulate and validate data."

JavaScript's syntax looks a lot like C, but it also include extra functionality to access and change your HTML, also known as the Document Object Model (DOM). 

You can use JavaScript directly in your HTML file in between <script></script> tags, or you can import your JavaScript as separate `.js` file.

Watch Brian Yu demonstrate using JavaScript in the CS50 IDE for an introduction.

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
  <iframe src="https://www.youtube.com/embed/WzfPjOYmjxg?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

## Getting Started
Here’s how to download this problem’s "distribution code" (i.e., starter code) into your own CS50 IDE. Log into [CS50 IDE](https://ide.cs50.io) and then, in a terminal window, execute each of the below.

1. Execute `wget https://intro.cs50nestm.net/wp-content/uploads/2020/02/temperature.zip` to download a (compressed) ZIP file with this problem’s distribution.
2. Execute `unzip temperature.zip` to uncompress that file.
3. Execute `rm temperature.zip` followed by `yes` or `y` to delete that ZIP file.
4. Execute `ls`. You should see a directory called `temperature`, which was inside of that ZIP file.
5. Execute `cd temperature` to change into that directory.
6. Execute `ls`. You should see this problem’s distribution code, including `index.html` and `styles.css`.
7. You can immediately start a server to view the site by typing

```
http-server
```

in the terminal window and clicking on the link that appears.

## Specification

This program uses HTML, CSS and JavaScript to create a temperature conversion web page, where you will convert Celsius to Fahrenheit and Fahrenheit to Celsius.

The HTML and CSS is already written for you, though you are welcome to customize it. Your challenge will be to write the JavaScript to make the program functional.

In between the

```html
<script>
</script>
```

tags, you will write JavaScript to access the value enterred into the text box, and depending on whether the user chooses `fahrenheit to celsius` or `celsius to fahrenheit` you will calculate the appropriate value and add it to the `div` with `id="result"` in `index.html`.

When the button is clicked, html will call the `convert()` function that you will write. 

## How to Start

You may want to create some shortcuts to be able to access the input value, the select value and the output area from your HTML. You can do this by creating three variables as follows:

```javascript
let input = document.querySelector("#tempInput")
let choice = document.querySelector("#choose")
let output = document.querySelector("#result")
```

Once the user enters a number in the text box, you can access the value with `input.value`. In the same way, you can access the value of the conversion choice with `choice.value`. Finally, you can add your own text to the `result` div by assigning the desired string to `output.innerHTML`.

Now write the function convert(). You can start this as:

```javascript
function convert() {
  // TODO

}
```

Remember this function will execute when the user clicks the `convert` button, so this would be a good time to get the number of degrees entered, the choice the user makes for conversion and test that these values are not blank. If either of these values is missing (when the choice is missing choice.value will be equal to "none") use a JavaScript alert to yell at the user and return from this function.

Now you can test if choice.value is equal to "ftoc" in which case you will want to calculate degrees celsius, or "ctof" in which you will want to calculate degrees fahrenheit. 

After performing the appropriate calculation, create a string using JavaScript concatenation that says something like:

```
100 degrees fahrenheit is 37.8 degrees celsius
```

Finally make sure your output uses exactly one decimal point for ease of reading.

## Hints

For fairly comprehensive guides on the languages introduced in this problem, check out the documentation for each on W3Schools.

* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css)
* [JavaScript](https://www.w3schools.com/js)

## How to Submit

Coming soon!
