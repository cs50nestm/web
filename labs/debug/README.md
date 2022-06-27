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
 
1. Compile (make) the program
2. The first error will probably say `debug.c:9:5: error: use of undeclared identifier 'name'`. The `9` after `debug.c:` means there is a problem on line 9. Why do you think is says `undeclared identifier`?
3. Look for things like missing symbols, missing libraries, missing variable declarations.
 
 
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




