#include <bits/stdc++.h>

using namespace std;

int main()
{
    int f;
    scanf("%d", &f);
    for (int i = 0; i < f; i++) {
        int n, x, a;
        long long total = 0;
        pair<int, int> value;
        scanf("%d %d", &n, &x);
        vector<pair<int, int>> values(n);
        for (int j = 0; j < n; j++) {
            scanf("%d", &a);
            values[j].first = a;
            values[j].second = 1;
        }
        for (size_t j = 0; j < values.size() and values[j].first % x == 0; j++) {
            values.push_back(make_pair(values[j].first / x, values[j].second * x));
        }
        for (size_t j = 0; j < values.size(); j++) {
            total += values[j].first * values[j].second;
        }
        printf("%lld\n", total);
    }
    return 0;
}
