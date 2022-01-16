#include <bits/stdc++.h>

using namespace std;

int n;
int loc;

int main() {
    cin >> n;
    int degrees[n];
    for (int i = 0; i < n; i++) {
        cin >> degrees[i];
    }
    for (int i = 0; i < (1 << n); i++) { // 1 << n == 2 ** n
        loc = 0;
        for (int j = 0; j < n; j++) { // check if jth bit is set
            if (i & (1 << j)) {
                loc += degrees[j];
            } else {
                loc -= degrees[j];
            }
        }
        if (!(loc % 360)) {
            cout << "YES" << "\n";
            return 0;
        }
    }
    cout << "NO" << "\n";
    return 0;
}
