import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    values, counts, ans = [int(i) % m for i in input().split()], {}, 0
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    for key in counts:
        if not key: # we group perfect divisors together
            ans += 1
        elif 2 * key == m: # we can group halves together
            ans += 1
        elif 2 * key < m or m - key not in counts:
            x, y = counts.get(key, 0), counts.get(m - key, 0) # m-divisible pair
            ans += 1 + max(0, abs(x - y) - 1) # sandwich key and m - key
    print(ans)
