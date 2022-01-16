#include <bits/stdc++.h>

using namespace std;

long long adj[501][501];
long long n;
long long m;
long long q;
long long a;
long long b;
long long c;
const long long big = 1e18;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m >> q;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            adj[i][j] = big;
        }
    }
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        adj[a][b] = min(adj[a][b], c);
        adj[b][a] = min(adj[b][a], c);
    }
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);
            }
        }
    }
    for (int i = 0; i < q; i++) {
        cin >> a >> b;
        if (a == b) {
            adj[a][b] = 0;
        }
        if (adj[a][b] < big) {
            cout << adj[a][b] << "\n";
        } else {
            cout << -1 << "\n";
        }
    }
    return 0;
}
