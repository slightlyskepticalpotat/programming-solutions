#include <bits/stdc++.h>

using namespace std;

int dp[30001][501], gems[30001];
int n, d, g;

int recurse(int i, int j) // max number of cumulative gems at (location, last jump)
{
    int ans = 0, offset = j - d + 250;
    if (i > 30000) {
        return 0;
    }
    if (dp[i][offset] != -1) {
        return dp[i][offset];
    }
    if (j == 1) {
        ans = gems[i] + max(recurse(i + j, j), recurse(i + j + 1, j + 1));
    } else { // minimum length last jump
        ans = gems[i] + max(max(recurse(i + j, j), recurse(i + j + 1, j + 1)), recurse(i + j - 1, j - 1));
    }
    dp[i][offset] = ans;
    return ans;
}

int main()
{
    for (int i = 0; i < 30001; i++) {
        for (int j = 0; j < 500; j++) {
            dp[i][j] = -1;
        }
    }
    for (int i = 0; i < 30001; i++) {
        gems[i] = 0;
    }
    scanf("%d %d", &n, &d);
    for (int i = 0; i < n; i++) {
        scanf("%d", &g);
        gems[g] += 1;
    }
    printf("%d\n", recurse(d, d));
}
