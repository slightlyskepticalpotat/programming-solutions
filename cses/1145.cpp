#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> values;
vector<int> dp;

int main() {
    cin >> n;
    while (cin >> n) { // trick to read all input
        values.push_back(n);
    }
    for (auto value: values) {
        int i = lower_bound(dp.begin(), dp.end(), value) - dp.begin(); // https://en.cppreference.com/w/cpp/algorithm/lower_bound
        if (i == dp.size()) { // we cen extend subsequence
            dp.push_back(value);
        } else {
            dp[i] = value;
        }
    }
    cout << dp.size() << "\n";
}
