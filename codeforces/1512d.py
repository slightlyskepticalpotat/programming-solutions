import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values, total, check, ans = int(input()), [int(i) for i in input().split()], 0, {}, [-1]
    for i in range(n + 2):
        total, check[values[i]] = total + values[i], check.get(values[i], 0) + 1
    for i in range(n + 2):
        test = values[i]
        check[test] = check.get(test, 0) - 1 # stop duplicates
        if (total - test) % 2 == 0 and check.get((total - test) // 2, 0):
            values.remove((total - test) // 2)
            values.remove(test)
            ans = values
            break
        check[test] += 1
    print(*ans)
