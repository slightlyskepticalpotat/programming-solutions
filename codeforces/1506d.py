import heapq, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values, num = int(input()), [int(i) for i in input().split()], {}
    for i in values:
        num[i] = num.get(i, 0) + 1
    final = [-num[i] for i in num if num[i]]
    heapq.heapify(final)
    while len(final) >= 2:
        a = heapq.heappop(final) + 1
        b = heapq.heappop(final) + 1
        if a:
            heapq.heappush(final, a)
        if b:
            heapq.heappush(final, b)
    if final:
        print(-final[0])
    else:
        print(0)
