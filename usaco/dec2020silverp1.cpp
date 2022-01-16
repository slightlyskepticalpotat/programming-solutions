#include <bits/stdc++.h>

using namespace std;

int dist[100001] = {0}, ans = 0;
vector<int> graph[100001];
queue<int> queuee;

void bfs(int start)
{
    queuee.push(start);
    dist[start] = 1;
    while (not queuee.empty()) {
        int searching = queuee.front(); queuee.pop();
        int uninfected = 0;
        for (int peer: graph[searching]) {
            if (dist[peer] == 0) {
                dist[peer] = 1;
                queuee.push(peer);
                uninfected += 1;
            }
        }
        ans += uninfected;
        if (uninfected > 0) {
            ans += ceil(log2(uninfected + 1));
        }
    }
}

int main()
{
    int n, a, b, centre = 0, max_peers = 0;
    scanf("%d", &n);
    for (int i = 0; i < n - 1; i++) {
        scanf("%d %d", &a, &b);
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    
    for (int i = 0; i < n; i++) {
        if (graph[i + 1].size() > max_peers) {
            max_peers = graph[i + 1].size();
            centre = i + 1;
        }
    }
    bfs(centre);
    printf("%d\n", ans);
}
