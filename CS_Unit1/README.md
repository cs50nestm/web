# Class Notes Unit 1

### Here is the code we developed together in class as a code-a-longs

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

#### First Submission: Hello, it's Me

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

#### Practice Problem: contacts.c

On Friday, we coded a practice problem, `contacts.c`  in another directory, this time called `practice`. The idea is to become comfortable with variables and printing using format codes.

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("Name: ");
    int age = get_int("Age: ");
    string phone = get_string("Phone: ");
    string location = get_string("Location: ");

    printf("New contact: %s, %i, lives in %s and can be reached at %s.\n", name, age, location, phone);
}
```

No submission required for this, but it will be a good reference for future programs.

#### Practice Problem: discount.c

This is a code-a-long problem that uses operators and calculates a value. It prints out a `float` with two decimal places. This may be helpful in completing your first PBA, `fahrenheit.c`.

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Ask user for regular price
    float regular = get_float("Regular Price: ");

    // Caluculate discount of 15%
    float sale = regular * 0.85;

    // Print out sale price
    printf("Sale Price: $%.2f\n", sale);
}
```

No submission required, but use as a reference for your PBA, **Fahrenheit**.

