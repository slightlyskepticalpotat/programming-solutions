#include <bits/stdc++.h>

using namespace std;

int n;
int a;
int b;
int x;
long long ans = LLONG_MIN;
multiset<long long> window;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> a >> b;
    vector<long long> psa(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> x;
        psa[i] = psa[i - 1] + x;
    }
    for (int i = a; i <= n; i++) { // iterate
        if (i > b) {
            window.erase(window.find(psa[i - b - 1])); // erase if too large
        }
        window.insert(psa[i - a]);
        ans = max(ans, psa[i] - *window.begin());
    }
    cout << ans << "\n";
    return 0;
}
