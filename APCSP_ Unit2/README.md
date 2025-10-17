# Unit 2 Notes

## Strings and Arrays: code-a-longs

### character.c
```c
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get User Input
    string text = get_string("Text: ");

    // Print character by character reverse order
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        printf("%i\n", text[i]);
    }
}
```

### alphabetical.c
```c
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // User Input
    string text = get_string("Text: ");

    // Iterate through string
    for (int i = 1, len = strlen(text); i < len; i++)
    {
        // Check if two consecutive chars out of order
        if (text[i - 1] > text[i])
        {
            // Short circuit the loop
            printf("Not in alpha order!\n");
            return 0;
        }
    }

    // We didn't return above so chars in order
    printf("In alpha order!\n");
}

```

### palindrome.c
```c
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get Input
    string s = get_string("Text: ");

    // Check chars from start and end
    for (int i = 0, len = strlen(s); i < len / 2; i++)
    {
        if (s[i] != s[len - i - 1])
        {
            printf("Not a palindome!\n");
            return 0;
        }
    }
    // Didn't return above so must be a palindrome
    printf("Palindrome!\n");
}
```

### anagram.c
```c
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    // Get two strings to compare
    string s1 = get_string("Word 1: ");
    string s2 = get_string("Word 2: ");

    // Declare array to keep track of number of occurances of 
    // each letter where `a` is `0`, `b` is `1`, etc.
    int characters[26] = {0};

    // Iterate througn s1 to add up occurances of each letter
    for (int i = 0, len = strlen(s1); i < len; i++)
    {
        // Check if this char is an alpha letter
        if (isalpha(s1[i]))
        {
            // Calculate index that corresponds to this letter
            int index = tolower(s1[i]) - 'a';

            // Increment element which corresponds to this letter
            characters[index]++;
        }
        else
        {
            // Found a non-alpha char, so return
            printf("Alpha chars only!\n");
            return 1;
        }
    }

    for (int i = 0, len = strlen(s2); i < len; i++)
    {
        if (isalpha(s2[i]))
        {
            // Here we subtract one for each occurrance of a letter
            int index = tolower(s2[i]) - 'a';
            characters[index]--;
        }
        else
        {
            printf("Alpha chars only!\n");
            return 1;
        }
    }

    // If we have an anagram all values in characters array should be 0
    for (int i = 0; i < 26; i++)
    {
        if (characters[i] != 0)
        {
            // Non-zero element means letters in the two words don't match
            printf("Not an anagram!\n");
            return 0;
        }
    }

    // We didn't return above so we have an anagram
    printf("Anagram!\n");
}
```
