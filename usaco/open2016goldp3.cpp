#include <bits/stdc++.h>

using namespace std;

int n;
int best;
int sequence[248];
int dp[248][248]; // dp[i][j] is the maximum value of the sequence starting at i and ending at j

int main() {
    freopen("248.in", "r", stdin); // cin.tie(0)->sync_with_stdio(0); unnecessary
    freopen("248.out", "w", stdout);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> sequence[i];
    }
    for (int j = 1; j <= n; j++) { // iterate on length
        for (int i = 0; i <= n - j; i++) {
            dp[i][i + j - 1] = -1; // i + j - 1 is the ending, we mark it as non mergeable
            if (j == 1) { // single element is just sequence[i]
                dp[i][i + j - 1] = sequence[i];
            }
            for (int k = i; k < i + j - 1; k++) {
                if (dp[i][k] == dp[k + 1][i + j - 1] && dp[i][k] > 0) { // if we can merge
                    dp[i][i + j - 1] = max(dp[i][i + j - 1], dp[i][k] + 1);
                }
            }
            best = max(best, dp[i][i + j - 1]);
        }
    }
    cout << best << "\n";
}
