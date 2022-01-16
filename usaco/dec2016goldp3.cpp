#include <bits/stdc++.h>

using namespace std;

int n;
int node;
int curr;
bool dir;

int main() {
    freopen("lasers.in", "r", stdin);
    freopen("lasers.out", "w", stdout);
    cin >> n;
    vector<pair<int, int>> mirrors(n + 2);
    map<int, vector<int>> lines[2];
    queue<pair<int, bool>> q;
    vector<int> dist(n + 2, INT_MAX);
    dist[0] = 0; // location of laser
    q.push({0, 1}); // 1 for horizontal
    q.push({0, 0}); // 0 for vertical
    for (int i = 0; i < n + 2; i++) { // count start and end as mirrors
        cin >> mirrors[i].first >> mirrors[i].second;
        lines[0][mirrors[i].first].push_back(i); // mark x coordinates
        lines[1][mirrors[i].second].push_back(i); // mark y coordinates
    }
    while (!q.empty()) {
        node = q.front().first;
        dir = q.front().second;
        q.pop();
        if (dir) { // switch direction
            curr = mirrors[node].first;
        } else {
            curr = mirrors[node].second;
        }
        for (auto peer: lines[!dir][curr]) {
            if (dist[peer] == INT_MAX) {
                q.push({peer, !dir});
                dist[peer] = dist[node] + 1;
            }
        }
    }
    if (dist[1] == INT_MAX) {
        cout << "-1" << "\n";
    } else {
        cout << dist[1] - 1 << "\n";
    }
    return 0;
}
