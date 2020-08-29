#include <stdio.h>

int main()
{
    int w, c;
    scanf("%d", &w);
    scanf("%d", &c);
    if (w == 3 and c >= 95) {
        printf("C.C. is absolutely satisfied with her pizza.\n");
    } else if (w == 1 and c <= 50) {
        printf("C.C. is fairly satisfied with her pizza.\n");
    } else {
        printf("C.C. is very satisfied with her pizza.\n");
    }
}