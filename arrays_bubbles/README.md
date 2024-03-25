# Arrays of Objects

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

Now add 100 bubble objects to your bubbles array by using a for loop!

## Extensions

Once you are successful in creating 100 jittering bubbles, see if you can add some additional functionality. 

Some ideas:

* Make each bubble change color when you click on it. (Hint: Check out the p5 function mouseClicked and dist for this one.)

* Make each bubble get bigger when you click on it.

* Make each bubble pop after clicking on it 3 times. (Hint: Look into the JavaScript function splice.)

* Create a new bubble when you click somewhere other than on another bubble.

To submit:

```
submit50 cs50nestm/checks/2023/arrays_bubbles
```

