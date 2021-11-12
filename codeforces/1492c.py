import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s, t = input().strip(), input().strip()
forward_index, reverse_index, i, j, ans = [], [], 0, 0, 0
while i < n and j < m:
    if s[i] == t[j]:
        forward_index.append(i)
        i, j = i + 1, j + 1
    else:
        i += 1
i, j = n - 1, m - 1
while i > -1 and j > -1:
    if s[i] == t[j]:
        reverse_index.append(i)
        i, j = i - 1, j - 1
    else:
        i -= 1
reverse_index = reverse_index[0:len(reverse_index) - 1][::-1] # omit last
for i in range(len(forward_index) - 1): # omit first
    ans = max(ans, reverse_index[i] - forward_index[i])
print(ans)
