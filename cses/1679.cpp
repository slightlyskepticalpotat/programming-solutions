#include <bits/stdc++.h>

using namespace std;

int n;
int m;
int a;
int b;
vector<int> toposort_order;
bool visited[100001];
vector<vector<int>> adj(100001);
vector<int> idx(100001);

void dfs(int node) {
    for (auto peer: adj[node]) {
        if (!visited[peer]) {
            visited[peer] = true;
            dfs(peer);
        }
    }
    toposort_order.push_back(node);
}
void toposort() {
    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            visited[i] = true;
            dfs(i);
        }
    }
    reverse(begin(toposort_order), end(toposort_order));
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        adj[a].push_back(b);
    }
    toposort();
    for (int i = 1; i <= n; i++) {
        idx[toposort_order[i]] = i;
    }
    for (int i = 1; i <= n; i++) {
        for (auto peer: adj[i]) {
            if (idx[peer] <= idx[i]) { // trust, but verify
                cout << "IMPOSSIBLE" << "\n";
                return 0;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        cout << toposort_order[i] << " ";
    }
    cout << "\n";
    return 0;
}
