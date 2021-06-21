#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, q, query, j;
    scanf("%d%d", &n, &q);
    vector<int> values(n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &values[i]);
    }
    for (int i = 0; i < q; i++) {
        scanf("%d", &query);
        j = find(values.begin(), values.end(), query) - values.begin();
        printf("%d ", j + 1);
        rotate(values.begin(), values.begin() + j, values.begin() + j + 1);
    }
    printf("\n");
}
