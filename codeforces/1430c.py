import math, heapq

for _ in range(int(input())):
    values, moves = [-(i + 1) for i in range(int(input()))], []
    heapq.heapify(values)
    for i in range(len(values) - 1):
        a, b = -heapq.heappop(values), -heapq.heappop(values)
        moves.append([a, b])
        heapq.heappush(values, -math.ceil((a + b) / 2))
    print(-heapq.heappop(values))
    for move in moves:
        print(*move)
