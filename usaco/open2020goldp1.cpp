#include <bits/stdc++.h>

using namespace std;

int n;
long long a;
long long inv[100001];
vector<long long> bit(100001);

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
    freopen("haircut.in", "r", stdin);
    freopen("haircut.out", "w", stdout);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a;
        inv[a + 1] += i - query(a + 1); // taller hairs
        update(a + 1, 1);
    }
    a = 0;
    for (int i = 1; i <= n; i++) {
        cout << a << "\n";
        a += inv[i];
    }
    return 0;
}
