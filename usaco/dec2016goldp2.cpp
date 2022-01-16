#include <bits/stdc++.h>

using namespace std;

int h;
int g;
int x;
int y;
vector<pair<int, int>> holsteins;
vector<pair<int, int>> guernseys;

int dist(pair<int, int> x, pair<int, int> y) {
    return (x.first - y.first) * (x.first - y.first) + (x.second - y.second) * (x.second - y.second);
}

int main() {
    freopen("checklist.in", "r", stdin);
    freopen("checklist.out", "w", stdout);
    cin >> h >> g;
    for (int i = 0; i < h; i++) {
        cin >> x >> y;
        holsteins.push_back(make_pair(x, y));
    }
    for (int i = 0; i < g; i++) {
        cin >> x >> y;
        guernseys.push_back(make_pair(x, y));
    }
    long long dp[2][h + 1][g + 1]; // dp[i][j][k] represents the minimum distance to visit holstein j and guernsey k, ending on holstein if i == 0 and guernsey otherwise
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < h + 1; j++) {
            for (int k = 0; k < g + 1; k++) {
                dp[i][j][k] = LLONG_MAX;
            }
        }
    }
    dp[0][1][0] = 0;
    for (int i = 0; i < h + 1; i++) {
        for (int j = 0; j < g + 1; j++) {
            if (i) { // holstein to holstein
                dp[0][i][j] = min(dp[0][i][j], dp[0][i - 1][j] + dist(holsteins[i - 1], holsteins[i - 2]));
            }
            if (j) { // guernsey to guernsey
                dp[1][i][j] = min(dp[1][i][j], dp[1][i][j - 1] + dist(guernseys[j - 1], guernseys[j - 2]));
            }
            if (i && j) { // holstein to guernsey and guernsey to holstein
                dp[0][i][j] = min(dp[0][i][j], dp[1][i - 1][j] + dist(holsteins[i - 1], guernseys[j - 1]));
                dp[1][i][j] = min(dp[1][i][j], dp[0][i][j - 1] + dist(holsteins[i - 1], guernseys[j - 1]));
            }
        }
    }
    cout << dp[0][h][g] << "\n";
    return 0;
}
