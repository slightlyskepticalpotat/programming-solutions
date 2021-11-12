n, staircase = int(input()), [int(i) for i in input().split()]
boxes, best = [[int(i) for i in input().split()] for _ in range(int(input()))], 0
for box in boxes:
    best = max(staircase[box[0] - 1], best)
    print(best)
    best += box[1] # only track leftmost stair
