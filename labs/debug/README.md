# Debugging

## Learning Goals
  * Become familiar with C Syntax
  * Learn what C compiler error messages mean
  * Get practice debugging



## Background

There are two kinds of errors that can occur when writing a program. The first errors you are likely to encounter are **syntactical** errors. In addition to syntactical errors, there can also be logical errors, which we'll take a look at soon.

In Computer Science, syntax is important for a computer to understand what you are telling it to do. Each programming language has its own syntactical rules, which include the combination of both words and punctuation. 

This lab starts with distribution code which has several syntactical errors. The idea is for you to try to compile (make) the program, learn to interpret the rather cryptic error messages output by the compiler, and **debug** the program.

<details>
 <summary>Hints</summary>
 
  1. The first error will probably see after trying to compile debug will be `debug.c:9:5: error: use of undeclared identifier 'name'`. The `9` after `debug.c:` means there is a problem on line 9. Why do you think is says `undeclared identifier`?
  2. You may want to look for errors such as missing symbols, missing libraries, missing variable declarations.
  3. If you are still stuck, try typing into the terminal `help50 make debug`.
 
 
</details>

## Demo

![DebugGif](https://raw.githubusercontent.com/cs50nestm/web/master/labs/debug/debugDemo.gif)
<!-- ![DebugGif](https://raw.githubusercontent.com/cs50nestm/web/master/labs/debug/debugDemo.gif | width=100) -->

<!-- <img src="https://raw.githubusercontent.com/cs50nestm/web/master/labs/debug/debugDemo.gif" width=100%>  -->


## Getting Started

1. Log into [code.cs50.io](https://code.cs50.io/) using your GitHub account. 
2. Click inside the terminal window and execute `cd`.
3. At the `$` prompt, type `mkdir labs1`
4. Now execute `cd labs1`
5. Then copy and paste `wget https://github.com/cs50nestm/web/raw/master/distro/debug.c` into your terminal to download this lab's distribution code.
6. Now try compiling this program, by typing `make debug` and see what happens!
7. You most likely see an error that says: `debug.c:9:5: error: use of undeclared identifier 'name'`
8. This means there is an error that has something to do with an undeclared identifier, on line 9. Fix this bug, and then try to compile again. Keep in mind that debugging is an iterative process. You may need to fix an error, compile, then fix another error, compile again, multiple times!

## Checking style

Before "submitting" any of your programs, you should always first check for correct style! Good style means your indentations and spacing are correct, which makes your code easier to read and debug. To do this, you can always type in `style50` into your terminal in front of the name of your `.c` file. But first, as when compiling, you must make sure your terminal is positioned in the correct directory.

```
style50 debug.c
```

## Submitting your completed program

TODO


