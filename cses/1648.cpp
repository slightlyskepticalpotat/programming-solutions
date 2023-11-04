#include <bits/stdc++.h>

using namespace std;

int n;
int q;
int t;
int a;
long long b;
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
    }
    for (int i = 0; i < q; i++) {
        cin >> t >> a >> b;
        if (t == 1) {
            update(a, -x[a]);
            x[a] = b;
            update(a, x[a]);
        } else {
            cout << query(b) - query(a - 1) << "\n";
        }
    }
    return 0;
}
