#include <bits/stdc++.h>

using namespace std;

int n;
int x;
stack<pair<int, int>> s;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n;
    s.push({0, 0}); // val[i], i
    for (int i = 0; i < n; i++) {
        cin >> x;
        while (!s.empty() && s.top().first >= x) { // pop until we get one smaller than x
            s.pop();
        }
        cout << s.top().second << " ";
        s.push({x, i + 1});
    }
    cout << "\n";
    return 0;
}
