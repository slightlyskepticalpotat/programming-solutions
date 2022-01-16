#include <bits/stdc++.h>

using namespace std;

map<char, int> idx;
string cowphabet;
int n;
int loc;

int main() {
    ios_base::sync_with_stdio(0); // fast io go brrr
    cin.tie(0);
    cin >> cowphabet;
    for (int i = 0; i < cowphabet.size(); i++) { // uniquely map each letter to a number
        if (!idx.count(cowphabet[i])) {
            idx[cowphabet[i]] = idx.size();
        }
    }
    n = idx.size(); // number of unique letters
    int adj[n][n] = {}; // frequency of different adjacent letters
    for (int i = 0; i < cowphabet.size() - 1; i++) {
        adj[idx[cowphabet[i]]][idx[cowphabet[i + 1]]] += 1;
    }
    int dp[1 << n] = {1}; // dp[i] is the minimum number of times if only the subset i exists, bessie hums at least once
    for (int i = 1; i < (1 << n); i++) {
        dp[i] = cowphabet.size(); // maximum times bessie hummed
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) { // if letter in subset
                loc = dp[i ^ (1 << j)]; // previous best
                for (int k = 0; k < n; k++) {
                    if (i & (1 << k)) { // if other letter in subset
                        loc += adj[j][k];
                    }
                }
                dp[i] = min(dp[i], loc); // minimise number of times
            }
        }
    }
    cout << dp[(1 << n) - 1] << "\n";
    return 0;
}
