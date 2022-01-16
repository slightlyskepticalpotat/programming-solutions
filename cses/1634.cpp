#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    int x;
    cin >> n >> x;
    vector<int> coins(n);
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }
    long long dp[1000001];
    dp[0] = 0;
    for (int i = 1; i <= x; i++) {
        dp[i] = INT_MAX;
        for (auto coin: coins) {
            if (i >= coin) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    if (dp[x] == INT_MAX) {
        dp[x] = -1;
    }
    cout << dp[x] << "\n";
}
