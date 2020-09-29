import sys

data = sys.stdin.readlines()
n, t, p = map(int, data[0].split())
scoring, contestants, scoreboard = [n] * t, [], []

for j in range(n):
    solved = [i for i in data[j + 1].split()]
    scoring = [scoring[i] - 1 if solved[i] == "1" else scoring[i] for i in range(t)]
    contestants.append(solved)

for i in range(n):
    scoreboard.append([sum(scoring[j] for j in range(t) if contestants[i][j] == "1"), contestants[i].count("1"), i + 1]) # score, tasks solved, number

scoreboard = list(sorted(scoreboard, key = lambda x: (x[0], x[1], -x[2]), reverse = True)) # reverse sort order
for i in range(n):  # detect phillip
    if p == scoreboard[i][2]:
        print(scoreboard[i][0], i + 1)