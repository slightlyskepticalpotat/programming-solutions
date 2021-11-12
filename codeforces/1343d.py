import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    vals, freqs, diff = [int(i) for i in input().split()], [0 for i in range(2 * k + 1)], [0 for i in range(2 * k + 2)]
    for i in range(n // 2): # frequency of each sum
        freqs[vals[i] + vals[n - i - 1]] += 1
    for i in range(n // 2): # range that we can cover
        diff[min(vals[i], vals[n - i - 1]) + 1] += 1
        diff[max(vals[i], vals[n - i - 1]) + 1 + k] -= 1
    for i in range(1, 2 * k + 2): # build the array
        diff[i] += diff[i - 1]
    ans = [diff[i] - freqs[i] + (n // 2 - diff[i]) * 2 for i in range(2, 2 * k + 1)] # change none, change one, change both
    print(min(ans))