# Problem: Temperature

## tl;dr
Complete the JavaScript code to add funcionality to a temperature conversion web page in the [CS50 IDE](https://ide.cs50.io).

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

tags, you will write JavaScript to access the value enterred into the text box, and depending on whether the user choosed `fahrenheit to celsius` or `celsius to fahrenheit` you will calculate the appropriate value and add it to the `div` with `id="result"` in `index.html`.

When the button is clicked, html will call the `convert()` function that you will write. 

## Writing JavaScript

Create some shortcuts to be able to access the input value, the select value and the output area from your HTML. You can do this by creating three variables as follows:

```javascript
let input = document.querySelector("#tempInput")
let choice = document.querySelector("#choose")
let output = document.querySelector("#result")
```
