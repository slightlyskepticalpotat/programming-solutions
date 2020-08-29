#include <math.h>
#include <stdio.h>

int main()
{
    int a, i;
    scanf("%d %d", &a, &i);
    for (int c = 0; c <= (i * a); c++) {
        if (ceil((double) c / a) == i) {
            printf("%d\n", c);
            exit (0);
        }
    }
}