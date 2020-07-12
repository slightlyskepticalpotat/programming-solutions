#include <stdio.h> // fast i/o

using namespace std;

int main() {
    int x, placeholder;
    int number = 0;
    scanf("%d", & x);
    for (int i = 1; i <= x; i++) {
        scanf("%d", & placeholder);
        number = number ^ placeholder;
    }
    printf("%d\n", number);
}