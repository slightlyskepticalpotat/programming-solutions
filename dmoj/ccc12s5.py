import sys
input = sys.stdin.readline

cats = []
rows, columns = map(int, input().split())
plan = [[0] * columns for _ in range(rows)] # build dp array
plan[0][0] = 1 # start
for i in range(int(input())):
    cats.append([int(i) for i in input().split()])
for thing in cats: # set cat cages
    plan[thing[0]-1][thing[1]-1] = -1

for i in range(rows):
    for j in range(columns):
        if plan[i][j] != -1:
            plan[i][j] = max(max(plan[i][j-1] + plan[i-1][j], plan[i][j]), max(plan[i][j-1], plan[i-1][j])) # max of self, left, top, left + top
print(plan[-1][-1])