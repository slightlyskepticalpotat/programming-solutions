#include <bits/stdc++.h>

using namespace std;

int n;
int m;
int a;
int b;
vector<int> cycle;
bool visited[100001];
bool toposort_order[100001];
vector<vector<int>> adj(100001);

bool dfs(int node) {
    visited[node] = true;
    toposort_order[node] = true;
    for (auto peer: adj[node]) {
        if (toposort_order[peer]) {
            cycle.push_back(node);
            toposort_order[node] = false;
            toposort_order[peer] = false;
            return true;
        } else if (!visited[peer]) {
            if (dfs(peer)) { // has cycle
                cycle.push_back(node);
                if (toposort_order[node]) {
                    toposort_order[node] = false;
                    return true;
                } else { // end cycle
                    return false;
                }
            }
            if (!cycle.empty()) {
                return false;
            }
        }
    }
    toposort_order[node] = false;
    return false;
}

void toposort() {
    for (int i = 1; i <= n; i++) {
        if (cycle.empty()) {
            dfs(i);
        }
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        adj[a].push_back(b);
    }
    toposort();
    if (cycle.empty()) {
        cout << "IMPOSSIBLE" << "\n";
    } else {
        reverse(begin(cycle), end(cycle));
        cout << cycle.size() + 1 << "\n";
        for (int i = 0; i < (int) cycle.size(); i++) {
            cout << cycle[i] << " ";
        }
        cout << cycle[0] << "\n";
    }
    return 0;
}
