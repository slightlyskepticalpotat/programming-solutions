import sys

input = sys.stdin.readline

n, values = int(input()), [int(i) for i in input().split()]
values, dp_arr = sorted(values), [0 for i in range(n)] # minimum ending at i
for i in range(n):
    for j in range(i - 1, -1, -1): # each substring
        dp_arr[j] = values[i] - values[j] + min(dp_arr[j + 1], dp_arr[j]) # add min or max
print(dp_arr[0])
