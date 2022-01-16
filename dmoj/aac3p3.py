import collections, sys

input = sys.stdin.readline

n, vals, low, high, ans, ans_str, x = int(input()), collections.deque(sorted([int(i) for i in input().split()])), collections.deque([]), collections.deque([]), [], [], -1
while vals:
    low.append(vals.popleft())
    if vals:
        high.append(vals.pop())
if len(low) > len(high):
    x = low.pop()
for i in range(len(low)):
    ans.append(low.popleft())
    ans.append(high.popleft())

for i in range(len(ans)):
    if ans[i] < ans[i - 1] or i == 0:
        ans_str.append("B")
    elif ans[i] > ans[i - 1] or i == len(ans) - 1:
        ans_str.append("S")
    else:
        ans_str.append("E")
if x != -1:
    ans.append(x)
    ans_str.append("E")
print(*ans)
print("".join(ans_str))