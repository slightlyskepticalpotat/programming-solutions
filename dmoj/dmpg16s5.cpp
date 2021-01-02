#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, k;
    long long ans = 0;
    deque<pair<long long, long long>> deck;
    scanf("%d %d", &n, &k);
    long long pizza[n * 2], psa[n * 2]; // this is a circle
    for (int i = 0; i < n; i++) {
        scanf("%lld", &pizza[i]);
        pizza[i + n] = pizza[i];
    }
    psa[0] = pizza[0];
    for (int i = 1; i < n * 2; i++) {
        psa[i] = psa[i - 1] + pizza[i];
    }
    for (int i = 1; i < n * 2; i++) { // largest sum segment
        while (not deck.empty() and deck.back().first >= psa[i]) {
            deck.pop_back();
        }
        deck.push_back({psa[i], i}); // keeps track of current sum and position
        if (deck.front().second < (i - k)) {
            deck.pop_front();
        }
        ans = max(ans, psa[i] - deck.front().first);
    }
    printf("%lld\n", ans);
}
// maximal sum of a subarray with a psa