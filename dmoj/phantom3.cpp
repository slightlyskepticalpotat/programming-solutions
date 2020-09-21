#include <math.h>
#include <stdio.h>
#include <vector>

using namespace std;

vector<long long> simple_prime_sieve (long long x)
{
    vector<long long> primes;
    bool sieve[x] = { 0 }; // inits all values, 0 means prime
    sieve[0] = 1;
    sieve[1] = 1;
    for (long long i = 2; i < x; i++) {
        if (not sieve[i]) {
            primes.push_back(i);
            for (long long j = i * i; j < x; j += i) {
                sieve[j] = 1;
            }
        }
    }
    return primes;
}

long long primes_in_range(long long x, long long y) // both ends closed
{
    long long num_primes = 0;
    bool sieve[y - x + 2] = { 0 };
    vector<long long> primes = simple_prime_sieve((long long) floor(sqrt(y)) + 2);
    for (long long i = 0; i < primes.size(); i++) { // minimum number in range multiple of prime
        long long limit = x / primes[i] * primes[i];
        if (limit < x) { // we underestimated
            limit += primes[i];
        }
        if (limit == primes[i]) { // we underestimated
            limit += primes[i];
        }
        for (long long j = limit; j < y + 1; j += primes[i]) {
            sieve[j - x] = 1;
        }
    }
    for(long long i = max((long long) 2, x); i < y + 1; i++) {
        if (not sieve[i - x]) {
            num_primes += 1;
        }
    }
    return num_primes;
}

int main()
{
    long long n, m;
    scanf("%lld%lld", &n, &m);
    printf("%lld\n", primes_in_range(max((long long) 2, n), m - 1));
    return 0;
}