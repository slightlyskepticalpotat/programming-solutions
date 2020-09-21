#include <numeric>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
    long n, m;
    scanf("%ld %ld", &n, &m);
    char s[1000001], t[1000001];
    scanf("%s %s", s, t); // be careful with format strings
    long len_s = (long) strlen(s), len_t = (long) strlen(t);
    long step = gcd(len_s, len_t), answer, freq[26];

    for (int i = 0; i < step; i++) { // o(s + t)
        for (int j = 0; j < 26; j++) { // set entire array to 0
            freq[j] = 0;
        }
        for (int j = 0; j < len_s / step; j++) { // record letter frequency
            freq[s[j * step + i] - 97] += 1;
        }
        for (int j = 0; j < len_t / step; j++) { // read letter frequency
            answer += freq[t[j * step + i] - 97]; // if same letter, the value isn't 0
        }
    }

    printf("%ld\n", answer * (step * m / len_s)); // expand to entire length
    return 0;
}