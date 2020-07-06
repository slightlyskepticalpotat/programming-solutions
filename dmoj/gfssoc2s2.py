import sys
input = sys.stdin.readline

cards, mana = map(int, input().split())
costs = []
for i in range(cards):
    card, cost = input().split()
    costs.append([card, int(cost)])
combos = []

for i in range(cards):
    for j in range(i + 1, cards):
        for k in range(j + 1, cards):
            if costs[i][1] + costs[j][1] + costs[k][1] <= mana:
                combos.append([costs[i][0], costs[j][0], costs[k][0]])
combos = sorted([sorted(char) for char in combos])
for thing in combos:
    print(*thing)