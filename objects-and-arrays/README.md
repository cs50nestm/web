# JavaScript Objects

An object is *one thing* that can be stored in one variable. An object can have many **properties**, think of these as additional variables stored inside the larger object.

That sounds pretty abstract, but it's not so bad, let's make a an object called `brick`:

```javascript
let brick = {x: 10, y: 100};
```

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

```javascript
student.favoriteColor = "blue"
```

#### Now Bubble Objects

Here is a program built with objects. 

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

# Arrays of Objects
