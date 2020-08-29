#include <math.h>
#include <stdio.h>

int x = 0;

int main()
{
    int m, k, n;
    scanf("%d %d %d", &m, &k, &n);
    if ((0.595 * n) - k > 0) {
        x = ceil((0.595 * n) - k);
    } else {
        x = 0;
    }
    if (x >= 0 and x <= m) { // possible to pass
        printf("%d\n", x);
    } else {
        printf("have mercy snew\n");
    }
}