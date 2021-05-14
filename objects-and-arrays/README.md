# JavaScript Objects and Arrays

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
### Why are Objects Important

Objects are a super important concept in programming and we've just scratched the surface here.

Objects allow us to group together into one container all the useful data that makes sense to be together.  This makes sense because it's like the real world, an object called `dog` might have `age`, `name`, `color`, and `weight` properties.

JavaScript objects are fundamental to how data from the internet is structured and retrieved.  If you wanted to make an app that used information about the current weather, movies playing near your zip-code, or just about any data you can imagine that comes from the internet, it is very, very likely that that data will be in the form of a big JavaScript object. With an understanding of objects, you're on your way to becoming an awesome developer.

## Arrays of Objects

Now let’s extend this to be able to handle 100 bubbles!

JavaScript arrays are used to store multiple values in a single variable. Now didn’t we say something like that about objects!

Well, yes and now. Objects if you remember store key-value pairs. Arrays store values in a list. Values in an array are accessed by their index, or their order in the array, starting with 0 for the first element in the array. For example:


```javascript
let teachers = ["Tanzosh", "Grima", "Park"]
```

In this case, teachers[0] has the value “Tanzosh”, teachers[1] has the value “Grima”, and teachers[2] has the value “Park”.

We can iterate through this list, (once it is created), access each element in order, by using this for loop:


```javascript
for (let teacher of teachers) {
  // do something
}
```

This would first access teacher[0], then teacher[1], then teacher[2].

An alternate way of iterating through a list (also useful for initially creating the list), is using a this type of a for loop:

```javascript
for (let i = 0; i < 100; i++) {
  // do something
}
```

This for loop has three parts: the initialization (let i = 0) which is executed once before the loop is executed, then the condition (i < 100), which must be true to execute the code inside the curly brackets (as you may have guessed, teachers.length is the length of the array), and i++ which is the update, which increases the value of i by one after each execution of the loop. All arrays in JavaScript have a .length method available, so you can use the condition i < teachers.length instead of i < 100 to iterate through as many teachers as you have in the array.

Now the cool thing is that arrays can store not only names, or numbers, but objects as well! So let’s make an array of bubbles!

To initialize your array variable, be sure to add:

```javascript
let bubbles = []
```

at the top of your program. You can add elements to an array in two ways. First create the object:

```javascript
bubble = {
  x: 10,
  y: 10
}
```
And then add it to a specific index:

```javascript
bubble[0] = bubble
```
Or additing it the end of the array:

```javascript
bubbles.push(bubble)
```

Now you can make many hundreds of bubbles!
