import sys

input = sys.stdin.readline

n, values = int(input()), list(sorted([int(i) for i in input().split()]))
if n <= 2: # at least one has to be c ** 0
    print(values[0] - 1)
else:
    ans = sum(values) - n
    for i in range(1, 10 ** 9): # power
        power, cost = 1, 0
        for j in range(n): # entire cost
            cost += abs(values[j] - power)
            power *= i
            if power > 10 ** 14: # max sum
                break
        if power > 10 ** 14 or power / i > ans + values[n - 1]: # max sum
            break
        ans = min(ans, cost)
print(ans)
