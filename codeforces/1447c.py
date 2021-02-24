import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, w = map(int, input().split())
    weights = [int(i) for i in input().split()]
    weights = sorted([[weights[i], i] for i in range(n)])
    index, total, target, flag = [], 0, math.ceil(w / 2), False
    for i in range(n):
        if weights[i][0] < target:
            total += weights[i][0]
            index.append(weights[i][1] + 1)
            if target <= total:
                print(len(index))
                print(*index)
                flag = True
                break
        elif target <= weights[i][0] <= w:
            print(1)
            print(weights[i][1] + 1)
            flag = True
            break
    if not flag:
        print(-1)
