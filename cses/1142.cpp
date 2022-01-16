#include <bits/stdc++.h>

using namespace std;

int n;
long long l = 0;
int j;
stack<pair<long long, long long>> s;
pair<long long, long long> c;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n;
    vector<int> k(n);
    for (int i = 0; i < n; i++) {
        cin >> k[i];
    }
    for (int i = 0; i < n; i++) {
        j = i;
        while (!s.empty() && k[i] < s.top().second) {
            c = s.top();
            s.pop();
            j = c.first;
            l = max(l, (i - c.first) * c.second);
        }
        s.push({j, k[i]});
    }
    while (!s.empty()) {
        c = s.top();
        s.pop();
        l = max(l, (n - c.first) * c.second);
    }
    cout << l << "\n";
    return 0;
}
