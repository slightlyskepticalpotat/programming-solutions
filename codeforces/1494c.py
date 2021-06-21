import sys

input = sys.stdin.readline

def solve(x, y): # initial, special
    n, m, ans = len(x), len(y), 0
    already, i, j = [0 for _ in range(n + 1)], 0, m - 1
    for i in range(n - 1, -1, -1): # boxes left at the end
        already[i] = already[i + 1]
        while j >= 0 and y[j] > x[i]:
            j -= 1
        if j >= 0 and y[j] == x[i]:
            already[i] += 1
    j = 0
    for k in range(m): # boxes pushed, first box ends on special
        while j < n and x[j] <= y[k] + j:
            j += 1
        while i < m and y[i] - y[k] < j:
            i += 1
        ans = max(ans, i - k + already[j])
    return ans

for _ in range(int(input())):
    n, m = map(int, input().split())
    initial, special = [int(i) for i in input().split()], [int(i) for i in input().split()] # next lines divide left and right
    initial_left, initial_right = [-initial[i] for i in range(n) if initial[i] < 0][::-1], [initial[i] for i in range(n) if initial[i] > 0]
    special_left, special_right = [-special[i] for i in range(m) if special[i] < 0][::-1], [special[i] for i in range(m) if special[i] > 0]
    print(solve(initial_left, special_left) + solve(initial_right, special_right))
