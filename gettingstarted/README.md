
## Class Notes

# Here is the code we developed together in class as a code-a-long

First Program: Hello

First we made a folder `hello` by typing `mkdir hello` into our terminal. Then we moved into that folder by changing director in the terminal, `cd hello`.

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


