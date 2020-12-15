#include <bits/stdc++.h>

using namespace std;

int n, m, u, v;
int path[100001], size_set[100001];
vector<int> result;

int find(int x) 
{ // find part of unite-find data structure
    if (x == path[x]) { // gets representative of set
        return x;
    }
    return path[x] = find(path[x]); // follows path
}

void unite(int x, int y) 
{ // union part of union-find data structure, union was taken
    x = find(x); // gets representatives
    y = find(y);
    if (size_set[x] < size_set[y]) { // find the bigger set
        swap(x, y);
    }
    size_set[x] += size_set[y]; // joins smaller set to bigger set
    path[y] = x;
}

int main()
{
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++) { // next element in path, size of component
        path[i] = i;
        size_set[i] = 1;
    }
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &u, &v);
        if (find(u) != find(v)) { // disjoint sets
            unite(u, v); // connect them
            result.push_back(i);
        }
    }
    for (int i = 1; i < n; i++) {
        if (find(i) != find(i + 1)) {
            printf("Disconnected Graph\n");
            return 0;
        }
    }
    for (int i = 0; i < result.size(); i++) {
        printf("%d\n", result[i] + 1);
    }
    return 0;
}