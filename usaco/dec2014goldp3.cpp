#include <bits/stdc++.h>

using namespace std;

long long n;
long long t;
long long p;
long long s;
vector<long long> cows;
multiset<long long> dp;

int main() {
    freopen("cowjog.in", "r", stdin);
    freopen("cowjog.out", "w", stdout);
    cin >> n >> t;
    for (long long i = 0; i < n; i++) {
        cin >> p >> s;
        cows.push_back(-(p + s * t)); // end pos
    }
    for (auto cow: cows) { // multiset to find longest non-decreasing subsequence
        auto i = dp.upper_bound(cow);
        if (i == dp.end()) {
            dp.insert(cow);
        } else {
            dp.erase(i);
            dp.insert(cow);
        }
    }
    cout << dp.size() << "\n";
    return 0;
}
