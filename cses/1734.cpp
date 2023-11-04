#include <bits/stdc++.h>

using namespace std;

int n;
int q;
int a;
int b;
int c;
int ans[200001];
vector<long long> bit(200001);
vector<long long> x(200001);
vector<pair<int, int>> queries[200001];
map<int, int> last;

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
    for (int i = 0; i < n; i++) { // record values
        cin >> x[i];
    }
    for (int i = 0; i < q; i++) { // store by start
        cin >> a >> b;
        queries[a].push_back({b, i});
    }
    for (int i = n; i >= 1; i--) {
        c = x[i - 1]; // current element
        if (last.count(c)) {
            update(last[c], -1); // no longer unique
        }
        last[c] = i; // latest occurrence
        update(i, 1); // unique starting here
        for (auto bi: queries[i]) { // for each query at queries[a]
            ans[bi.second] = query(bi.first); // ans[i] = query(b)
        }
    }
    for (int i = 0; i < q; i++) {
        cout << ans[i] << "\n";
    }
    return 0;
}
