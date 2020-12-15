// see python version for comments

#include <bits/stdc++.h>

using namespace std;

int n;
long long pop[200002], inn[200002], out[200002], connections, best;
vector<int> roads[200002], reversed_roads[200002];
bool searched_in[200002], searched_out[200002];

long long dfs_in(int x)
{
    searched_in[x] = true;
    long long current = pop[x];
    for (auto peer: reversed_roads[x]) {
        if (not searched_in[peer]) {
            current += dfs_in(peer);
        } else {
            current += inn[peer];
        }
    }
    inn[x] = current;
    return current;
}

long long dfs_out(int x)
{
    searched_out[x] = true;
    long long current = pop[x];
    for (auto peer: roads[x]) {
        if (not searched_out[peer]) {
            current += dfs_out(peer);
        } else {
            current += out[peer];
        }
    }
    out[x] = current;
    return current;
}

int main()
{
    int u, v;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &pop[i + 1]);
    }
    for (int i = 0; i < n - 1; i++) {
        scanf("%d %d", &u, &v);
        roads[u].push_back(v);
        reversed_roads[v].push_back(u);
    }

    for (int i = 0; i < n; i ++) {
        if (not searched_in[i + 1]) {
            dfs_in(i + 1);
        }
        if (not searched_out[i + 1]) {
            dfs_out(i + 1);
        }
    }

    for (int i = 0; i < n; i++) {
        for (auto peer: reversed_roads[i + 1]) {
            best = max(best, (out[peer] - out[i + 1]) * (inn[i + 1] - inn[peer]));
        }
    }
    for (int i = 0; i < n; i++) {
        out[i + 1] -= pop[i + 1];
    }
    for (int i = 0; i < n; i++) {
        connections += pop[i + 1] * out[i + 1];
        connections += pop[i + 1] * (pop[i + 1] - 1);
    }
    printf("%lld\n", connections + best);
}