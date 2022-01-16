#include <bits/stdc++.h>

using namespace std;

int n;
int a = 0;
int r = -1;
set<int> s;
int k[200001];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> k[i];
    }
    for (int l = 0; l < n; l++) { // iterate on starting point
        while (r < n - 1 && !s.count(k[r + 1])) { // if unique and in bound
            r += 1;
            s.insert(k[r]); // add to set
        }
        a = max(a, r - l + 1); // record size
        s.erase(k[l]); // erase duplicate element at start
    }
    cout << a << "\n";
    return 0;
}
