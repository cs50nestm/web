# Debugging

## Learning Goals
  * Become familiar with C Syntax
  * Learn what C compiler error messages mean
  * Get practice debugging

## Background

There are two kinds of errors that can occur when writing a program. The first errors that students are likely to encounter are **syntactical** errors. In addition to syntactical errors, there can also be logical errors, which we'll take a look at soon.

In Computer Science, syntax is important for a computer to understand what you are telling it to do. Each programming language has its own syntactical rules, which include the combination of both words and punctuation. 

This lab starts with distribution code which has several syntactical errors. The idea is for students to try to compile (make) the program, learn to interpret the rather cryptic error messages output by the compiler, and **debug** the program.

## Getting Started

1. Log into [code.cs50.io](https://code.cs50.io/) using your GitHub account. 
2. Click inside the terminal window and execute `cd`.
3. At the `$` prompt, type `mkdir labs1`
4. Now execute `cd labs1`
5. Then copy and paste `wget https:////github.com/cs50nestm/web/raw/master/distro/debug.c` into your terminal to download this lab's distribution code.
6. Now try compiling this program, by typing `make debug` and see what happens!
7. You most likely see several errors. Your job now is to decipher these error messages, and debug the program.



