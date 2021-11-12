import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    plan = [[char for char in input().strip()] for i in range(n)]
    count_a, inv_a, count_b, inv_b = 0, [], 0, []
    if plan[0][1] == "1":
        inv_a.append([1, 2])
        count_a += 1
    if plan[1][0] == "1":
        inv_a.append([2, 1])
        count_a += 1
    if plan[n - 2][n - 1] == "0":
        inv_a.append([n - 1, n])
        count_a += 1
    if plan[n - 1][n - 2] == "0":
        inv_a.append([n, n - 1])
        count_a += 1
    if plan[0][1] == "0":
        inv_b.append([1, 2])
        count_b += 1
    if plan[1][0] == "0":
        inv_b.append([2, 1])
        count_b += 1
    if plan[n - 2][n - 1] == "1":
        inv_b.append([n - 1, n])
        count_b += 1
    if plan[n - 1][n - 2] == "1":
        inv_b.append([n, n - 1])
        count_b += 1
    if count_a <= count_b:
        print(count_a)
        for inv in inv_a:
            print(*inv)
    else:
        print(count_b)
        for inv in inv_b:
            print(*inv)
