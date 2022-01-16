#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> values;
multiset<int> dp;

int main() {
    cin >> n;
    while (cin >> n) { // trick to read all input
        values.push_back(n);
    }
    for (auto value: values) { // multiset to find longest non-decreasing subsequence
        auto i = dp.upper_bound(value);
        if (i == dp.end()) {
            dp.insert(value);
        } else {
            dp.erase(i);
            dp.insert(value);
        }
    }
    cout << dp.size() << "\n";
}
