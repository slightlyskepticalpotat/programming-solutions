#include <bits/stdc++.h>

using namespace std;

int n;
int m;
int a;
int b;
int c;
long long ans = 0;
int path[100001];
int length[100001];
vector<vector<long long>> edges;

int find(int x) {
    if (x == path[x]) {
        return x;
    }
    return path[x] = find(path[x]);
}

int unite(int x, int y) {
    x = find(x);
    y = find(y);
    if (length[y] > length[x]) {
        swap(x, y);
    }
    length[x] += length[y];
    path[y] = x;
    return length[x];
}

int main() { // kruskal mst
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        path[i] = i;
        length[i] = 1;
    }
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        edges.push_back({c, a, b});
    }
    sort(edges.begin(), edges.end());
    for (auto edge: edges) {
        if (find(edge[1]) != find(edge[2])) {
            ans += edge[0];
            unite(edge[1], edge[2]);
        }
    }
    if (length[find(1)] != n) {
        cout << "IMPOSSIBLE" << "\n";
    } else {
        cout << ans << "\n";
    }
    return 0;
}
