#include <bits/stdc++.h>

using namespace std;

int n;
int q;
int t;
int a;
int b;
int u;
int k;
vector<long long> bit(200001);
vector<long long> x(200001);

void update(int index, long long value) {
    while (index <= n) {
        bit[index] += value;
        index += (index & -index); // isolate least sig bit
    }
}

long long query(int index) {
    long long value = 0;
    while (index >= 1) {
        value += bit[index];
        index -= (index & -index); // isolate least sig bit
    }
    return value;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> q;
    for (int i = 1; i <= n; i++) {
        cin >> x[i];
        update(i, x[i]);
        update(i + 1, -x[i]);
    }
    for (int i = 0; i < q; i++) {
        cin >> t;
        if (t == 1) {
            cin >> a >> b >> u;
            update(a, u);
            update(b + 1, -u);
        } else {
            cin >> k;
            cout << query(k) << "\n";
        }
    }
    return 0;
}
