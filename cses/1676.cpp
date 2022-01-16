#include <bits/stdc++.h>

using namespace std;

int n;
int m;
int a;
int b;
int largest = 1;
int path[100001];
int length[100001];

int find(int x) {
    if (x == path[x]) {
        return x;
    }
    return path[x] = find(path[x]);
}

int unite(int x, int y) { // returns size of bigger component
    x = find(x);
    y = find(y);
    if (length[y] > length[x]) {
        swap(x, y);
    }
    length[x] += length[y];
    path[y] = x;
    return length[x];
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        path[i] = i;
        length[i] = 1;
    }
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        if (find(a) != find(b)) {
            largest = max(largest, unite(a, b));
            n -= 1;
        }
        cout << n << " " << largest << "\n";
    }
    return 0;
}
