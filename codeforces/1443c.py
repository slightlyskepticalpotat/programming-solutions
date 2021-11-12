import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, total, i, best, delivery, pickup = int(input()), 0, 0, float("inf"), [int(i) for i in input().split()], [int(i) for i in input().split()]
    times = sorted([[delivery[i], pickup[i]] for i in range(n)], key = lambda x: x[0], reverse = True)
    while i < n:
        if total > times[i][0]: # pickup is better
            best = min(best, total)
            break
        if total + times[i][1] >= times[i][0]: # delivery is better
            best = min(best, times[i][0])
            break
        total, i = total + times[i][1], i + 1
    print(min(best, sum(pickup)))
