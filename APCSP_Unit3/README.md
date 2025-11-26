# Unit 3 Notes

## Sorting and Searching Code-a-longs

### bubble.c

### selection.c

### binary.c

### max.c

### candidates.c
```c
#include <cs50.h>
#include <stdio.h>

typedef struct
{
    string name;
    int votes;
} candidate;

candidate candidates[3];

candidate get_candidate(void);

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        candidates[i] = get_candidate();
    }

    // Let print out the winner(s) highest votes
    // First find the max votes for any candidate
    int max = 0;
    for (int i = 0; i < 3; i++)
    {
        if (candidates[i].votes > max)
        {
            max = candidates[i].votes;
        }
    }
    
    // Print out candidates with the max votes
    for (int i = 0; i < 3; i++)
    {
        if (candidates[i].votes == max)
        {
            printf("Most Votes: %s\n", candidates[i].name);
        }
    }
}

candidate get_candidate(void)
{
    // Declare new candidate
    candidate new_candidate;

    // Assign attributes
    new_candidate.name = get_string("Name: ");
    new_candidate.votes = get_int("Votes: ");

    // Return
    return new_candidate;
}

```
