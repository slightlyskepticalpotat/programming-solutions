#include <bits/stdc++.h>

using namespace std;

int n;
int x;
const int MOD = 1000000007;
int dp[1000001];

int main() {
    cin >> n >> x;
    vector<int> coins(n);
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    dp[0] = 1;
    for (auto coin: coins) { // loops reversed from challenge 1635
        for (int i = 1; i <= x; i++) {
            if (i >= coin) {
                dp[i] += dp[i - coin];
                dp[i] %= MOD;
            }
        }
    }
    cout << dp[x] << "\n";
}
