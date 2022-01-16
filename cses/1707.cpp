#include <bits/stdc++.h>

using namespace std;

int n;
int m;
int a;
int b;
int node;
int ans = INT_MAX;

int main() {
    cin.tie(0)->sync_with_stdio(0);;
    cin >> n >> m;
    vector<vector<int>> adj(n + 1);
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
        edges[i] = make_pair(a, b);
    }
    for (auto edge: edges) { // we remove each edge since the length of a cycle is the distance from point a to another point b, plus 1 to get from b to a
        vector<int> dist(n + 1, INT_MAX);
        queue<int> q;
        dist[edge.first] = 0;
        q.push(edge.first);
        while (!q.empty()) {
            node = q.front();
            q.pop();
            for (auto peer: adj[node]) {
                if (dist[peer] == INT_MAX && !(node == edge.first && peer == edge.second)) { // remove the edge
                    dist[peer] = dist[node] + 1;
                    q.push(peer);
                }
            }
        }
        if (dist[edge.second] != INT_MAX) {
            ans = min(ans, dist[edge.second] + 1);
        }
    }
    if (ans == INT_MAX) {
        ans = -1;
    }
    cout << ans << "\n";
    return 0;
}
