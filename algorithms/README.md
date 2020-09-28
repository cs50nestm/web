# Writing Problem: Everyday Algorithms

## tl;dr

Write up algorithms to exhaustively describe in text and pseudocode, 
steps to brush one’s teeth, eat an orange, and something you do everyday.


## Step 1: Watch This.

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


Let’s start off by watching David’s video (from Ted-ED) on Algorithms.

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/6hfOvs8pY1k?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""> </iframe>
</div>

As we see from that video, algorithms are sets of instructions for completing a task step-by-step. Sometimes these algorithms can be quite simple. One way to express an algorithm for deciding how to dress based on the weather might be to say something like this.

```
Look out the window. If it is raining outside, put on 
your rain boots and raincoat. Then go outside.
```

## Step 2: Read This.

The concept of an algorithm is fundamental in computer science. Recall from earlier in this chapter that we defined a computer as a device that accepts input, and processes it in some way to produce a result automatically. The critical word in that sentence when we are talking about algorithms is the word "processes".

Say you’re playing your favorite video game of all time. If you’re a fan of nostalgia, it might be this gem.


<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/zNBwkI0ytZo?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allowfullscreen="allowfullscreen"> </iframe>
</div>


Assume you’re racing Sonic around Green Hill Zone and you see a couple of rings up in the air, over Sonic’s head. Because they protect you in the event you are attacked by an enemy, you want to pick them up. In order to grab them, you have to press one of the buttons on the controller. When you press that button, Sonic jumps into the air to a consistent height. When and if he touches the ring, it disappears from the screen so it cannot be claimed multiple times, and the number of rings in his possession—​indicated by a ring counter—​increases by one.


Every step of that process involved multiple algorithms. Described informally, those algorithms (greatly simplified) might read as something like this:

```
If the jump button is pressed and if Sonic is standing 
on the ground, begin moving him upward until he reaches 
the top of his arc. After he reaches the top of his arc, 
begin moving him downward by simulating gravity's pull 
until he is standing on the ground again.
```

And for the rings:

```
If Sonic is touching a ring, remove the ring from the 
screen and increase Sonic's ring counter by one.
```

Let’s focus just on the jumping algorithm for now, because the "input" to that algorithm is a lot clearer. The device that is executing this algorithm is the Sega Genesis console (or, more likely nowadays, an emulator for the same) running the Sonic the Hedgehog software. What is the data or input? That would be you, holding your controller, pressing down on the button that makes Sonic jump. (In fact, as you may recall, it’s actually an electrical pulse that occurred when you pressed that button that likely "jump-started" this algorithm.[2])

What is the result? On the television screen or monitor you see Sonic’s height off the ground begin to change; what he looks like might begin to change, too. Instead of keeping the same appearance as he did when standing on the ground, typically when Sonic jumps his sprite (a term we’ll be seeing again soon) changes to a ball that rotates, indicating that his jump is actually more of a flip or somersault through the air. As in reality, one doesn’t jump off the ground and then just fly off into the sky. What goes up must come down and so eventually after reaching the top of his jump Sonic lands on the ground again.

All of this is a process. And, truly, the process is a lot more fine-grained than that. We’ve oversimplified for purposes of illustration. We’ve also glossed over the notion of multiple algorithms running simultaneously in separate threads (another term we’ll be seeing again soon). But hopefully this example suffices for now.

Because this process of what happens when the jump button is pressed can be described as a clear, unambiguous, series of steps (aka, algorithmically)—at least in the game’s source code—it is consistent and, importantly, repeatable. If Sonic is standing at the same point and we press the jump button again and again—if he is standing on the ground and nothing else gets in his way like an enemy, whose algorithm might at some point fly them over Sonic’s head—the result is the same, again and again. Sonic always jumps to the same height, he spins in the same way while jumping, and he lands on the ground after the same amount of time. Because of the jumping algorithm, the computer always knows exactly what to do when that jump button is pressed, and always does exactly what it is told to do.

Sometimes it is easiest to express an algorithm using common language. That’s what we have done so far. Look back to the very first algorithm mentioned above—about deciding what to wear in the event of rain. Maybe there’s a way to articulate the decision-making process of getting ready more clearly?

Instead of this:

```
Look out the window. If it is raining outside, put on 
your rain boots and raincoat. Then go outside.
```

you might see a computer scientist instead use what’s called pseudocode—short expressions in common language organized in a way that resembles what source code looks like—to write their algorithms. We’ll talk more about pseudocode soon, but getting in the habit of writing it before you dive into actual coding in Scratch, C, PHP, or JavaScript is a great idea, much like writing the first draft of an essay.



Here’s one possible way to translate that algorithm into pseudocode:

```
1   look out the window
2   if it is raining outside
3      put on your rain boots
4      put on your raincoat
5   go outside
```

We’ve numbered the lines for a reason you’ll see momentarily. But notice how regardless of whether it’s raining the algorithm instructs you to go outside. It just has a special extra set of things you do before stepping outside if it happens to be raining. We call something like "if it is raining outside" a condition. Some algorithms also have steps that get repeated many times over, like this one:

```
Secretly pick your favorite number from 1 to 50. When your friend gives you a number, if they are too
high tell them to guess lower and if they are too low tell them to guess higher. If they are right,
have your friend stop guessing.
```

We call such a repetition a loop, because you’ll keep going around and around the same steps until some condition (your friend guessing the right number) lets you stop. Here’s one of many possible ways to express the guessing game in pseudocode:

```
 1   secretly pick your favorite number from 1 to 50
 2   have your friend guess your favorite number
 3   if your friend guesses a lower number
 4      tell your friend to guess a higher number
 5      go back to line 2
 6   else if your friend guesses a higher number
 7      tell your friend to guess a lower number
 8      go back to line 2
 9   else
10      tell your friend to stop guessing
```

Notice here that until your friend guesses the correct number, they will go back to line 2 of the algorithm, which prompts them to make another guess. Only when they guess correctly can they proceed to line 10 and *break* out of the loop.


## Step 3: Write This.

Okay, now you’ve learned a lot about algorithms and pseudocode. Perhaps we should try writing a few—​three, to be precise. Write your pseudocode in the file ‘algorithms.txt’ on the right (or a google doc then copy and then pasting into this file). First, write up algorithms (both in **sentence form** and in **pseudocode**) for how to:

* brush one’s teeth
* eat an orange

Next, think of something that you do every day or nearly every day. Write an algorithm in sentence form and in pseudocode for how to do the thing you’re thinking of.

If you’re stuck, know that you aren’t just limited to purely text-based ways of writing out algorithms when trying to come up with them. It may help to just get started with a simple flowchart, such as the one Sheldon Cooper used in this clip from TV’s *The Big Bang Theory*:

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/k0xgjUhEG3U?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allowfullscreen="allowfullscreen"> </iframe>
</div>


Just do your best to avoid any infinite loops (a loop that’s impossible to ever break out of) in your algorithm, lest you be stuck in one forever!


## Step 4: Do This.

Now for a little bit of fun. Before you actually turn in your algorithms, you probably should have someone test them out. Here’s what happened in a recent iteration of CS50 when making a peanut butter and jelly sandwich using an algorithm supplied by students.

<div class="iframe_container">
  <iframe src="https://www.youtube.com/embed/wEdvGqxafq8?modestbranding=1&amp;rel=0&amp;showinfo=0" frameborder="0" allowfullscreen="allowfullscreen"> </iframe>
</div>


As you can see, describing algorithms precisely is crucial in order to have the desired effect! Have a few friends or family members test out your algorithms, instructing them to make absolutely no assumptions beyond exactly what you’ve written. Is your algorithm described clearly enough that your set of instructions can be repeated exactly without any ambiguity as to what to do? Did your friend or family member find a way to break your algorithm or, worse, find themselves in an infinite loop?

If so, help them escape, then take another crack at rewriting your algorithm’s instructions to see if you can’t make it a bit clearer.

Go back to the first paragraph of this section and run through those steps again.

See what we did there?

This process may actually be more challenging than it first appears, and that’s okay. We promise though, once you start writing source code you’ll have access to a new (but limited!) toolkit of keywords and commands that will make precise algorithm-writing substantially easier!


## How to Submit

To come.

