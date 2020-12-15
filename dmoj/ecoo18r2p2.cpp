#include <bits/stdc++.h>

using namespace std;

vector<double> placeholder[1000001];
priority_queue<double> assignments;
double w, r, ans;
int n, d;

int main()
{
    for (int i = 0; i < 10; i++) {
        for (int m = 0; m < 1000001; m++) {
            placeholder[m] = vector<double>(); // empty vector
        }
        assignments = priority_queue<double>(); // empty priority queue
        ans = 0;
        scanf("%d", &n);
        for (int j = 0; j < n; j++) {
            scanf("%d %lf", &d, &w);
            placeholder[d].push_back(w);
        }

        for (int k = 1000000; k >= 1; k--) { // best task for each day
            for (auto l: placeholder[k]) {
                assignments.push(l);
            }
            if (not assignments.empty()) {
                r = assignments.top(); assignments.pop(); // needed
                ans += r;
            }
        }
        printf("%.4lf\n", ans);
    }
    return 0;
}