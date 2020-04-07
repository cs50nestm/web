# JavaScript Objects

The goal of this project is to create bubbles that are JavaScript Objects.

![bubbles](https://s3.amazonaws.com/upperline/curriculum-assets/p5js/monkey-bubbles.gif)

We'll be making some bubbles that wobble over the screen! If that doesn't excite you on it's own you should definitely get excited about all the learning you will be doing because by then end you will have some really powerful tools in your programmer's tool belt.


## A First Attempt

![bubbles](https://s3.amazonaws.com/upperline/curriculum-assets/p5js/bubbles.gif)

That image shows several bubbles. Last week when we started looking at p5.js we made a single bubble with code that looks something like this. 

```javascript
let bubbleSize = 20;

let bubble1X, bubble1Y;

function setup() {
  createCanvas(500,400);
  bubble1X = random(0, width);
  bubble1Y = random(0, height);
}

function draw() {
  background(0);
  fill(250);

  circle(bubble1X, bubble1Y, bubbleSize);

  bubble1X += random(-2, 2);
  bubble1Y += random(-2, 2);
}
```

Now go ahead and add a 100 bubbles...

Just kidding, that would take ages, your hands would be cramped, and you probably wouldn't learn all that much.

One thing that I'm thinking ahead about is that it seems like every time I'd want to add one new bubble, it would require two new variables. But, those two variables are clearly associated with each other. `bubble1X` and `bubble1Y` for example. Every new bubble adds (at least) 2 new variables.

What if we could group those related variables together into one. A bubble is *one thing*, so shouldn't we have it represented in our code as *one variable*. Ideally, a single variable `bubble1` could *store both pieces of data* the `x` and `y`. That would cut our number of variables in half, or even less!

## JavaScript Objects

The way we can do this is with **JavaScript Objects**. An object is *one thing* that can be stored in one variable. An object can have many **properties**, think of these as additional variables stored inside the larger object.

That sounds pretty abstract, but it's not so bad, let's make a an object called `brick`:

![first object](http://intro2018.cs50nestm.net/wp-content/uploads/2019/04/brick.gif)

Nice, the object we created with this code has two properties, `x` and `y`.

```javascript
let brick = {x: 10, y: 100};
```
#### Creating Objects

We create objects using curly braces

```javascript
let emptyObject = {};
```

#### Properties, {key: value}

Properties are added inside of an object. A property has two main parts, a *name* and a *value*.  This is very much like a variable, `x = 3`, the name is `x` the value is `3`.

With objects the name to a property is called a **key**.  You will often hear people refer to properties and their values as *key-value pairs*. The object below has one key-value pair, the key is `firstName` and the value is `"Jenny"`:

```javascript
let student = {firstName: "Jenny"};
```

#### Multiple Properties

When there are multiple properties in an object, they are separated by commas. Often objects will be written across multiple lines. Either way is fine as long as your commas and braces are in the right place.

```javascript
let student = {firstName: "Jenny", grade: 11};
// or
let student = {
  firstName: "Jenny",
  grade: 11
};
```


#### Accessing Properties

We've seen how new objects are created, but we will also need to *access* the values inside of objects. We do this with a dot (a period `.`) after the object name.

`student.firstName` gives us back the value `"Jenny"`.

`student.grade` gives us back the value `11`.

#### Adding Properties

You can also use the same *dot* after the object name plus an `=` to add additional properties to an object after it's created or to change existing properties

![adding properties](http://intro2018.cs50nestm.net/wp-content/uploads/2019/04/objects.gif)

## Now with Objects

Here's the same program as above built with objects. This may not seem like a huge change from before, but we're headed in the right direction.

```javascript
let bubbleSize = 20;

let bubble1;

function setup() {
  createCanvas(500,400);
  bubble1 = {
    x: random(0, width),
    y: random(0, height)
  };
}

function draw() {
  background(0);
  fill(250);

  circle(bubble1.x, bubble1.y, bubbleSize);

  bubble1.x += random(-2, 2);
  bubble1.y += random(-2, 2);
}
```
## Why are Objects Important

Objects are a super important concept in programming and we've just scratched the surface here.

Objects allow us to group together into one container all the useful data that makes sense to be together.  This makes sense because it's like the real world, an object called `dog` might have `age`, `name`, `color`, and `weight` properties.

JavaScript objects are fundamental to how data from the internet is structured and retrieved.  If you wanted to make an app that used information about the current weather, movies playing near your zip-code, or just about any data you can imagine that comes from the internet, it is very, very likely that that data will be in the form of a big JavaScript object. With an understanding of objects, you're on your way to becoming an awesome developer.

## Getting Started

1. Execute `cd` to ensure that you’re in ~/ (i.e., your home directory, aka ~).
2. Execute `wget https://intro.cs50nestm.net/wp-content/uploads/2020/04/bubbles.zip` to download a (compressed) ZIP file with this problem’s distribution.
1. Execute `unzip bubbles.zip` to uncompress that file.
1. Execute `rm bubbles.zip` followed by yes or y to delete that ZIP file.
1. Execute ls. You should see a directory called `bubbles`, which was inside of that ZIP file.
1. Execute `cd bubbles` to change into that directory.
1. Execute ls. You should see this problem’s distribution code, including index.html, style.css and sketch.js


## Specification

1. Starting with the code above, add at least one more bubble and make it an object.

2. Add a `size` property to each bubble object. The size can be random or hard-coded in.

3. Add a `color` property to every bubble object that is a random number between `0` and `255`. Use that number to make the bubbles `fill` a random grayscale color.

  You don't have to worry that the property `color` will conflict with p5's built-in `color` function.  This is because you will be accessing it by something like `bubble1.color`. The property `color` is sort of protected inside the object.

4. Wouldn't it be cool if the bubbles were a random color that wasn't gray. One way to do this would be to make 3 new properties inside each object. The keys could be `r`, `g`, and `b` perhaps, and the values a random value.

  If you're up for a challenge, one interesting thing is that a key of an object can have a value that is *another object*.  What if you're bubble looked like:
  ```javascript
  bubble = {
    x: ...,
    y: ...,
    color: {
      r: ...,
      g: ...,
      b: ...
    }
  }
  ```

The way you would access the `g` key would be `bubble.color.g`.  Give it a shot!

## To Submit

Coming Soon!

(Lesson above was adapted from a front-end design class given by Upperline Code)
