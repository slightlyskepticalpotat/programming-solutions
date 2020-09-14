import sys

input = sys.stdin.readline

scores, ranks, first, last = [], [], 0, 0
for i in range(int(input())):
    score, rank = map(float, input().split())
    scores.append(score)
    ranks.append(rank)
your_score = float(input())
zipped = sorted(zip(scores, ranks), key = lambda x: x[0], reverse = True)

for i in range(len(zipped)):
    if i == 0:
        left = 1
        right = zipped[i][1] * 2 - 1
    else:
        left = right + 1
        right = 2 * abs(zipped[i][1] - left) + left
    if zipped[i][0] == your_score:
        print(int(left))
        print(int(right))
        raise SystemExit