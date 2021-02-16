#include <cs50.h>
#include <stdio.h>

bool search(int value, int values[], int start, int end);

int main(void)
{
    // Define sorted array
    int values[] = {-1, 2, 3, 5, 7, 10, 15, 21, 32, 50};

    // Get input
    int value = get_int("Enter a number: ");

    // Define start and end values to begin searching
    int start = 0;
    int end = 9;

    // Check if input value is found
    if (search(value, values, start, end))
    {
        printf("Found!\n");
    }
    else
    {
        printf("Not found!\n");
    }
}

bool search(int value, int values[], int start, int end)
{
    // TODO
    return false;
}
