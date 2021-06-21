import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s = int(input()), input().strip()
    d_f, k_f, cnt, ans = 0, 0, {}, 0
    for i in range(n):
        if s[i] == "D":
            d_f += 1
        else:
            k_f += 1
        loc_d_f, loc_k_f = d_f // (math.gcd(d_f, k_f)), k_f // (math.gcd(d_f, k_f))
        cnt[(loc_d_f, loc_k_f)] = cnt.get((loc_d_f, loc_k_f), 0) + 1
        print(cnt[(loc_d_f, loc_k_f)], end = " ")
    print("")
