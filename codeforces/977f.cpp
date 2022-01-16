#include <bits/stdc++.h>

using namespace std;

int n;
int x;
int best = 0;
int best_i = 0;
vector<int> ans;
map<int, int> dp;

int main() {
    cin >> n;
    vector<int> values(n);
    for (int i = 0; i < n; ++i) {
        cin >> values[i];
    }
    for (int i = 0; i < n; ++i) {
        x = values[i];
        dp[x] = dp[x - 1] + 1; // dp[i] is the answer for last element i
        if (best < dp[x]) {
            best = dp[x];
            best_i = x;
        }
    }
    for (int i = n - 1; i >= 0; --i) {
        if (values[i] == best_i) {
            ans.push_back(i);
            best_i -= 1;
        }
    }
    reverse(ans.begin(), ans.end());
    cout << best << "\n";
    for (auto i: ans) {
        cout << i + 1 << " "; // 0 vs 1 indexing
    }
    cout << "\n";
}
