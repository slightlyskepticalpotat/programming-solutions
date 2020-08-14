import sys
input = sys.stdin.readline

yodellers, rounds = map(int, input().strip().split())
scores = [[0, 0, i + 1] for i in range(yodellers)] # score, worst rank

for _ in range(rounds):
    buffer = [int(i) for i in input().split()]
    for i in range(yodellers): # update scores
        scores[i][0] += buffer[i]
    for i in range(yodellers):
        if scores[i][1] < len([char for char in scores if char[0] > scores[i][0]]) + 1: # rankings
            scores[i][1] = len([char for char in scores if char[0] > scores[i][0]]) + 1
scores.sort(key = lambda x: x[0], reverse=True) # first sort by score
winners = [char for char in scores if char[0] == scores[0][0]]
winners.sort(key = lambda x: x[2]) # then yodeller number
for thing in winners:
    print(f"Yodeller {thing[2]} is the TopYodeller: score {thing[0]}, worst rank {thing[1]}")