#include <cs50.h>
#include <stdio.h>

bool search(int value, int values[], int start, int end);

int main(void)
{
    int values[] = {-1, 2, 3, 5, 7, 10, 15, 21, 32, 50};
    
    int value = get_int("Enter a number: );
    
    int start = 0;
    int end = 9;
    
    if (search(value, values, start, end))
    {
        printf("Found!\n");
    }
    else
    {
        printf("Not found!");
    }
}

bool search(int value, int values[], int start, int end)
{
    // TODO
}
