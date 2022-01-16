#include <bits/stdc++.h>

using namespace std;

int n;
int k;
int r = -1;
int ans_l;
int ans_r;
int ans = 0;
int a[500001];
int f[1000001];
set<int> s;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int l = 0; l < n; l++) {
        while (r < n - 1 && (int) s.size() + (f[a[r + 1]] == 0) <= k) {
            r += 1;
            s.insert(a[r]);
            f[a[r]] += 1;
        }
        if (ans < (r - l + 1)) {
            ans = r - l + 1;
            ans_l = l;
            ans_r = r;
        }
        f[a[l]] -= 1;
        if (f[a[l]] == 0) {
            s.erase(a[l]);
        }
    }
    cout << ans_l + 1 << " " << ans_r + 1 << "\n";
    return 0;
}
