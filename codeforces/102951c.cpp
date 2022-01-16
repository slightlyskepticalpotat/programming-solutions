#include <bits/stdc++.h>

using namespace std;

int n;

vector<int> lis(vector<int> values) {
    vector<int> dp; // will eventually have the lis
    for (auto value: values) {
        int i = lower_bound(dp.begin(), dp.end(), value) - dp.begin(); // https://en.cppreference.com/w/cpp/algorithm/lower_bound
        if (i == dp.size()) { // we cen extend subsequence
            dp.push_back(value);
        } else {
            dp[i] = value;
        }
    }
    return dp;
}

int main() {
    cin >> n;
    vector<int> a(n);
    vector<int> b(n);
    vector<int> cor(n); // cor[i] = idx[b[i]]
    int idx[n]; // a[idx[x]] = x
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        idx[a[i]] = i;
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }
    for (int i = 0; i < n; i++) { // increasing subsequences in c correspond to a common subsequence between a and b
        cor[i] = idx[b[i]];
    }
    cout << lis(cor).size() << "\n";
}
