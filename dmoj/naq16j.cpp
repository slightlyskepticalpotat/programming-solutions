#include <stdio.h>
#include <string.h>

int main() {
    int n;
    char number[102];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", number);
        printf("%d\n", (int) strlen(number));
    }
    return 0;
}