import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values, ans = int(input()), list(sorted([int(i) for i in input().split()])), []
    ans.append(values[-1] * values[-2] * values[-3] * values[-4] * values[-5])
    if 0 in values:
        ans.append(0)
    values.sort(key = lambda x: abs(x), reverse = True)
    for i in range(5):
        product = 1
        for j in range(5): # workaround around dividing by 0
            if j != i:
                product *= values[j]
        ans.extend([product * values[k] for k in range(5, n)])
    ans.append(values[0] * values[1] * values[2] * values[3] * values[4])
    print(max(ans))
