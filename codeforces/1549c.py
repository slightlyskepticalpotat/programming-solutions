import sys

input = sys.stdin.readline

n, m = map(int, input().split())
weaker = [0 for i in range(n + 1)] # weaker[i] is the number of friends i is weaker than
for i in range(m):
    u, v = map(int, input().split())
    weaker[min(u, v)] += 1
winners = weaker.count(0) - 1

for i in range(int(input())):
    q = [int(i) for i in input().split()]
    if q[0] == 1:
        update = min(q[1], q[2])
        if weaker[update] == 0:
            winners -= 1
        weaker[update] += 1
    elif q[0] == 2:
        update = min(q[1], q[2])
        weaker[update] -= 1
        if weaker[update] == 0:
            winners += 1
    else:
        print(winners)