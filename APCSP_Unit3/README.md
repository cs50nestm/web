# Unit 3 Notes

## Sorting and Searching Code-a-longs

### bubble.c
```c
// complete the bubble_sort function

#include <cs50.h>
#include <stdio.h>

// function prototypes
void bubble_sort(int arr[], int size);
void print_array(int arr[], int size);a

// size of array
#define SIZE 10

int main(void)
{
    // initialize array
    int arr[] = {1, 8, 4, 6, 0, 3, 5, 2, 7, 9};

    // sort array
    bubble_sort(arr, SIZE);

    // print out the array
    print_array(arr, SIZE);

    // done
    return 0;
}

// Function to print an array
void print_array(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("\n");
}

// bubble sort
void bubble_sort(int arr[], int size)
{
    // TODO
    for (int i = 0; i < size - 1; i++)
    {
        bool swaps = false;
        for (int j = 0; j < size - 1 - i; j++)
        {
             // See if left element is more than right
            if (arr[j] > arr[j + 1])
            {
                // Out of order so swap them
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swaps = true;
            }
        }
        if (swaps == false) {
            // We're done it's sorted
            return;
        }
    }
}
```

### selection.c
```c
// complete the selection_sort function

#include <cs50.h>
#include <stdio.h>

// function prototypes
void selection_sort(int arr[], int size);
void print_array(int arr[], int size);

// size of array
#define SIZE 10

int main(void)
{
    // initialize array
    int arr[] = {1, 8, 4, 6, 0, 3, 5, 2, 7, 9};

    // sort array
    selection_sort(arr, SIZE);

    // print out the array
    print_array(arr, SIZE);

    // done
    return 0;
}

// Function to print an array
void print_array(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("\n");
}

// selection sort
void selection_sort(int arr[], int size)
{
    // TODO
    for (int i = 0; i < size - 1; i++)
    {
        // Assume min values is at arr[min]
        int min = i;
        for (int j = i + 1; j < size; j++)
        {
            if (arr[j] < arr[min])
            {
                min = j;
            }
        }
        // Swap arr[i] with arr[min]
        int temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}
```

### binary.c
```c
// implement binary search function

#include <cs50.h>
#include <stdio.h>

#define NUMBERS 9

bool bin_search(int value, int values[], int size);

int main(void)
{
    int arr[] = {2, 4, 6, 7, 8, 11, 14, 18, 20};

    int target = get_int("Enter a number: ");

    if (bin_search(target, arr, NUMBERS))
    {
        printf("Found\n");
    }
    else
    {
        printf("Not found!\n");
    }
}

bool bin_search(int value, int values[], int size)
{
    // TODO
    int min = 0;
    int max = size - 1;

    while (min <= max)
    {
        int middle = (min + max) / 2;

        if (value == values[middle])
        {
            return true;
        }
        else if (value < values[middle])
        {
            max = middle - 1;
        }
        else
        {
            min = middle + 1;
        }
    }

    return false;
}
```

### max.c
```c
// Practice writing a function to find a max value

#include <cs50.h>
#include <stdio.h>

int max(int array[], int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number of elements: ");
    }
    while (n < 1);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        arr[i] = get_int("Element %i: ", i);
    }

    printf("The max value is %i.\n", max(arr, n));
}

// TODO: return the max value
int max(int array[], int n)
{
    int max = array[0];

    for (int i = 1; i < n; i++)
    {
        if (array[i] > max)
        {
            max = array[i];
        }
    }
    return max;
}
```

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
