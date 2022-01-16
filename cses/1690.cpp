#include <bits/stdc++.h>

using namespace std;

int n;
int m;
int a;
int b;
const int mod = 1000000007;
long long dp[1 << 20][21]; // dp[i][j] is the number of routes through subset i that end at city j
vector<int> adj[21]; // adj[i] is a vector of the cities that can reach i

int main() { // we need to turn permutations into subsets
    cin.tie(0); // fast input in cpp
    ios_base::sync_with_stdio(0);
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        adj[b].push_back(a);
    }
    dp[1][1] = 1; // 1 way to traverse subset {1} ending at city 1

    for (int i = 2; i < (1 << n); i++) { // 1 << n == 2 ** n
        if ((i & (1 << (n - 1))) && (i != ((1 << n) - 1))) { // skip if we don't end at city n
            continue;
        }
        for (int j = 1; j <= n; j++) { // loop through each city
            if (!(i & (1 << (j - 1)))) { // skip if city not in subset
                continue;
            }
            for (auto k: adj[j]) { // backtrack for each previous city
                if (i & (1 << (k - 1))) { // if previous city in subset
                    dp[i][j] += dp[i - (1 << (j - 1))][k]; // add number of paths to reach previous city
                    dp[i][j] %= mod;
                }
            }
        }
    }
    cout << dp[(1 << n) - 1][n] << "\n"; // use entire subset, end at n
    return 0;
}
