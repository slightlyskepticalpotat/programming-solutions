#include <bits/stdc++.h>

using namespace std;

long long smallest(long long n)
{
    for (long long i = n; i <= (n + 2520); i++) {
        long long temp = i;
        bool possible = true;
        while (temp) {
            if (temp % 10 != 0) {
                long long digit = temp % 10;
                if (i % digit != 0) {
                    possible = false;
                    break;
                }
            }
            temp /= 10;
        }
        if (possible) {
            return i;
        }
    }
}

int main()
{
    int n;
    long long k;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &k);
        printf("%lld\n", smallest(k));
    }
    return 0;
}
