#include <bits/stdc++.h>

using namespace std;

int n;
int x;

int main() {
    cin >> n >> x;
    vector<int> price(n);
    vector<int> pages(n);
    for (int i = 0; i < n; i++) {
        cin >> price[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> pages[i];
    }

    vector<vector<int>> dp(n + 1, vector<int>(x + 1, 0)); // dp[n][x] is maximum with n items, x dollars
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= x; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j >= price[i - 1]) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - price[i - 1]] + pages[i - 1]); // previous max vs taking new item
            }
        }
    }
    cout << dp[n][x] << "\n";
}
