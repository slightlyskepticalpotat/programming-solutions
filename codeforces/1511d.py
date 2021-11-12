import sys

input = sys.stdin.readline

n, k = map(int, input().split())
string, ans = "abcdefghijklmnopqrstuvwxyz", ""
for i in range(k): # all 2 letter substrings
    j = i # since same 2 letter substrings increase score
    while True:
        ans, j = ans + string[j], j + 1
        if j == k:
            break
        ans += string[i]
while len(ans) < n:
    ans *= 2
print(ans[:n])
