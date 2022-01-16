#include <bits/stdc++.h>

using namespace std;

int n;
int m;
int a;
int b;
int node;
deque<int> p;
queue<int> q;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m;
    vector<int> dist(n + 1, INT_MAX);
    vector<int> parent(n + 1);
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    dist[1] = 1;
    q.push(1);
    while (!q.empty()) {
        node = q.front();
        q.pop();
        for (auto peer: adj[node]) {
            if (dist[peer] == INT_MAX) {
                dist[peer] = dist[node] + 1;
                parent[peer] = node;
                q.push(peer);
            }
        }
    }
    if (dist[n] == INT_MAX) {
        cout << "IMPOSSIBLE";
    } else {
        cout << dist[n] << "\n";
        a = dist[n];
        for (int i = 0; i < a; i++) {
            p.push_front(n);
            n = parent[n];
        }
        for (int i = 0; i < p.size(); i++) {
            cout << p[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}
