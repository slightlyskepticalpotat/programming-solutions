#include <bits/stdc++.h>

using namespace std;

int n, m, x, y, s, t;
int dist[1000001];
vector<int> adj[1000001];
queue<int> queuee;

void bfs(int start)
{
    queuee.push(start);
    dist[start] = 0;
    while (not queuee.empty()) {
        int searching = queuee.front(); queuee.pop();
        for (int thing: adj[searching]){
            if (dist[thing] == -1) {
                queuee.push(thing);
                dist[thing] = dist[searching] + 1;
            }
        }
    }
}

int main()
{
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &x, &y);
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    fill_n(dist, 1000001, -1);
    scanf("%d %d", &s, &t);
    bfs(s);
    printf("%d\n", m - dist[t]);
}