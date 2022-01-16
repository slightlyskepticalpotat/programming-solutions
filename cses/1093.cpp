#include <bits/stdc++.h>

using namespace std;

int n;
int total;
const int MOD = 1000000007;

int main() {
    cin >> n;
    total = n * (n + 1) / 2;
    if (total % 2) {
        cout << 0 << "\n";
        return 0;
    }
    total /= 2;
    int dp[n][total + 1] = {}; // dp[i][j] is ways to make j with i coins
    dp[0][0] = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= total; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j >= i) {
                dp[i][j] += dp[i - 1][j - i];
                dp[i][j] %= MOD;
            }
        }
    }
    cout << dp[n - 1][total] << "\n";
}
