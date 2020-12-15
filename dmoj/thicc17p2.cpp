#include <cstdio>

long long n, a, b, m, all_sum, sum_square;

int main()
{
    scanf("%lld %lld %lld %lld", &n, &a, &b, &m);
    for (int i = 0; i < n; i++) {
        all_sum += a;
        sum_square += a * a;
        a *= b;
        all_sum %= 1000000007;
        sum_square %= 1000000007;
        a %= m;
    }
    printf("%lld\n", (all_sum * all_sum - sum_square) % 1000000007);
    return 0;
}