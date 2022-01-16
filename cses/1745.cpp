#include <bits/stdc++.h>

using namespace std;

int n;

int main() {
    cin >> n;
    vector<int> coins(n);
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }
    bool dp[n + 1][100001]; // dp[i][j] true if sum j with i coins
    dp[0][0] = true;

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= 100000; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j >= coins[i - 1] && dp[i - 1][j - coins[i - 1]]) {
                dp[i][j] = true;
            }
        }
    }
    vector<int> possible;
    for (int i = 1; i <= 100000; i++) {
        if (dp[n][i]) {
            possible.push_back(i);
        }
    }
    cout << possible.size() << "\n";
    for (auto value: possible) {
        cout << value << " ";
    }
    cout << "\n";
}
