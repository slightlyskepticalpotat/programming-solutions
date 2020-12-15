#include <bits/stdc++.h>

using namespace std;

int n, mi;
char instruction[5], ci[6];
priority_queue<int> blue, pink, green;

int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s ", instruction);
        if (*instruction == 'A') { // first char of char array
            scanf("%s %d\n", ci, &mi);
            if (*ci == 'B') {
                blue.push(-mi);
            } else if (*ci == 'P') {
                pink.push(-mi);
            } else {
                green.push(-mi);
            }
        } else {
            if (not blue.empty()) {
                mi = blue.top(); blue.pop();
                printf("%s %d\n", "BLUE", -mi);
            } else if (not pink.empty()) {
                mi = pink.top(); pink.pop();
                printf("%s %d\n", "PINK", -mi);
            } else if (not green.empty()) {
                mi = green.top(); green.pop();
                printf("%s %d\n", "GREEN", -mi);
            } else {
                printf("NONE\n");
            }
        }
    }
    return 0;
}