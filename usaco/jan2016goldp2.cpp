#include <bits/stdc++.h>

using namespace std;

int n;
int m;
int start_loc[4];
string f_path;
string b_path;
vector<pair<int, int>> f_loc;
vector<pair<int, int>> b_loc;
map<char, vector<int>> moves{{'N', {0, 1}}, {'E', {1, 0}}, {'S', {0, -1}}, {'W', {-1, 0}}};

int dist(pair<int, int> x, pair<int, int> y) {
    return (x.first - y.first) * (x.first - y.first) + (x.second - y.second) * (x.second - y.second);
}

int main() {
    freopen("radio.in", "r", stdin);
    freopen("radio.out", "w", stdout);
    cin >> n >> m;
    cin >> start_loc[0] >> start_loc[1] >> start_loc[2] >> start_loc[3];
    cin >> f_path >> b_path;
    int dp[n + 1][m + 1]; // dp[i][j] represents the minimum distance on move i for farmer john after i moves and bessie after j moves
    for (int i = 0; i < n + 1; i++) { // fill grid with max value
        for (int j = 0; j < m + 1; j++) {
            dp[i][j] = INT_MAX;
        }
    }
    f_loc.push_back(make_pair(start_loc[0], start_loc[1]));
    b_loc.push_back(make_pair(start_loc[2], start_loc[3]));
    for (int i = 0; i < n; i++) {
        f_loc.push_back(make_pair(f_loc[i].first + moves[f_path[i]][0], f_loc[i].second + moves[f_path[i]][1]));
    }
    for (int i = 0; i < m; i++) {
        b_loc.push_back(make_pair(b_loc[i].first + moves[b_path[i]][0], b_loc[i].second + moves[b_path[i]][1]));
    }
    dp[0][0] = 0;
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < m + 1; j++) {
            dp[i][j - 1] = min(dp[i][j - 1], dp[i - 1][j - 1] + dist(f_loc[i], b_loc[j - 1]));
            dp[i - 1][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + dist(f_loc[i - 1], b_loc[j]));
            dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + dist(f_loc[i], b_loc[j]));
        }
    }
    cout << dp[n][m] << "\n";
}
