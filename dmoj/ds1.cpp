// kind of like a dynamic variant of a prefix sum original_array, all operations o(logn)
// we use two binary indexed trees here for frequency and value

#include <bits/stdc++.h>

using namespace std;

int n, m, x, y, original_array[100002];
long long values[100002], frequencies[100002];
char operation;

void update(long long tree[], int index, int value) // adds value to element at index of tree
{
    while (index <= 100002) {
        tree[index] += value;
        index += (index & -index); // isolate least significant bit
    }
}

long long query(long long tree[], int index) // sum of all elements up to index of tree
{
    long long value = 0;
    while (index >= 1) {
        value += tree[index];
        index -= (index & -index); // isolate least significant bit
    }
    return value;
}

int main()
{
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &original_array[i]);
        update(values, i, original_array[i]); // add to the values tree
        update(frequencies, original_array[i], 1);
    }

    for (int i = 0; i < m; i++) {
        scanf(" %c", &operation); // hack to ignore leading whitespace
        if (operation == 'C') {
            scanf("%d %d", &x, &y);
            update(frequencies, original_array[x], -1);
            update(values, x, y - original_array[x]);
            update(frequencies, y, 1);
            original_array[x] = y;
        } else if (operation == 'S') {
            scanf("%d %d", &x, &y);
            printf("%lld\n", query(values, y) - query(values, x - 1));
        } else if (operation == 'Q') {
            scanf("%d", &x);
            printf("%lld\n", query(frequencies, x));
        }
    }
    return 0;
}