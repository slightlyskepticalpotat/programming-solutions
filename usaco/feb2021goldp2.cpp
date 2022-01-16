#include <bits/stdc++.h>

using namespace std;

int n;
int colours[300];
int dp[300][300]; // dp[i][j] is the minimum answer from i to j

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> colours[i];
    }
    for (int i = 0; i < n; i++) { // worst case scenario
        for (int j = 0; j < n; j++) {
            dp[i][j] = 300;
        }
    }
    for (int i = 0; i < n; i++) { // one colour needed
        dp[i][i] = 1;
    }
    for (int j = 0; j < n; j++) { // iterate on length
        for (int i = 0; i < n - j; i++) { // iterate on start
            for (int k = i; k < i + j; k++) { // iterate on merge
                if (colours[i] == colours[i + j]) { // if we can merge
                    dp[i][i + j] = min(dp[i][i + j], dp[i][k] + dp[k + 1][i + j] - 1); // reduce number of colours by 1
                }
                dp[i][i + j] = min(dp[i][i + j], dp[i][k] + dp[k + 1][i + j]); // simply add sides together
            }
        }
    }
    cout << dp[0][n - 1] << "\n";
    return 0;
}
