# Class Notes

### Here is the code we developed together in class as a code-a-long

#### First Program: Hello

We started by typing into the terminal to create a folder `hello` by executing `mkdir hello` next to the `$` prompt. Then we moved into that folder by changing director in the terminal, `cd hello`.

We created a new code file in that folder, `hello.c` by typing `code hello.c`.

Finally we typed in the following code in our code editors.

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}

```

To execute this program, we first must compile it:

```
make hello
```

and finally execute it as

```
./hello
```

No submission required for this.

#### First PBA: Hello, it's Me

In a new folder named `me` we created the next program. 

```
cd
mkdir me
cd me
code hello.c
```

This new version of hello takes and input and outputs hello to you!

```c
#include <cs50.h>
#include <stdio.h>
int main(void)
{
    string name = get_string("What is your name? ");
    printf("hello, %s\n", name);
}
```

This program should be submited, using the line starting with `submit50` in the problem spec.

#### Practice Problem: print.c

Together, we coded a practice problem, `print.c`  in another directory, this time called `practice`. The idea is to become comfortable with variables and printing using format codes.

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for a name
    string name = get_string("Name: ");

    // Prompt for age
    int age = get_int("Age: ");

    // Prompt for Phone Number
    string phone = get_string("Phone Number: ");

    // Print name, age and phone number (%s for strings, %i for ints)
    printf("My name is %s, I'm %i years old and my phone is %s\n", name, age, phone);
}
```

No submission required for this, but it will be a good reference for future programs.

#### Practice Problem: calculator0.c through calculator4.c

Don't worry if your programs are named differently! These are for practice and reference.

calculator0.c

```c
// Addition with integer

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for an x
    int x = get_int("x: ");

    // Prompt for a y
    int y = get_int("y: ");

    // Add numbers
    int z = x + y;

    // Print sum
    printf("%i\n", z);
}
```

calculator1.c

```c
// Addition with integer, without third variable

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for an x
    int x = get_int("x: ");

    // Prompt for a y
    int y = get_int("y: ");

    // Print sum
    printf("%i\n", x + y);
}
```

calculator2.c

```c
// Multiply a number

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for an x
    int x = get_int("x: ");

    // Double it
    printf("%i\n", x * 2);
}
```

calculator3.c

```c
// Divide 2 ints

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for an x
    int x = get_int("x: ");

    // Prompt for a y
    int y = get_int("y: ");

    // Print integer division
    printf("%i\n", x / y);
}
```

calculator4.c

```c
// Divide 2 floats

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for an x
    float x = get_float("x: ");

    // Prompt for a y
    float y = get_float("y: ");

    // Print floating point division
    printf("%f\n", x / y);
}
```

These are code-along practice problems, and do not need to be submitted.

#### discount.c

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for regular price
    float regular = get_float("Regular Price: ");

    // Calculate discount
    float sale = regular * 0.85;

    // Print sale price
    printf("Sale Price: $%.2f\n", sale);
}
```

#### conditionals.c

Practice using `if-else` statements.

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("x: ");
    int y = get_int("y: ");

    if (x > y)
    {
        printf("x is greater than y\n");
    }
    else if (y > x)
    {
        printf("y is greater than x\n");
    }
    else
    {
        printf("x is equal to y\n");
    }
}
```

### sum.c

Practice using a `for` loop.

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int sum = 0;
    for (int i = 0; i < 10; i++)
    {
        int n = get_int("Number: ");
        sum = sum + n;
    }
    printf("Sum: %i\n", sum);
}
```
