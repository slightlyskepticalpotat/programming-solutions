// 2d binary indexed tree; basically a dynamic prefix minimum array

#include <bits/stdc++.h>

using namespace std;

int s, x, y, a, l, b, r, t, operation, values[1025][1025];

void twod_update(int x, int y, int value)
{
    for (int i = x; i <= s; i += i & -i) {
        for (int j = y; j <= s; j += j & -j) {
            values[i][j] += value;
        }
    }
}

int twod_query(int x, int y)
{
    int value = 0;
    for (int i = x; i >= 1; i -= i & -i) {
        for (int j = y; j >= 1; j -= j & -j) {
            value += values[i][j];
        }
    }
    return value;
}

int main()
{
    while (true) {
        scanf("%d", &operation);
        if (operation == 0) {
            scanf("%d", &s);
        } else if (operation == 1) {
            scanf("%d %d %d", &x, &y, &a);
            twod_update(x + 1, y + 1, a);
        } else if (operation == 2) {
            scanf("%d %d %d %d", &l, &b, &r, &t);
            printf("%d\n", twod_query(r + 1, t + 1) - twod_query(r + 1, b) - twod_query(l, t + 1) + twod_query(l, b)); // ahh
        } else if (operation == 3) {
            return 0;
        }
    }
}