import sys
input = sys.stdin.readline

plan = []
rows, columns = map(int, input().strip().split())
for i in range(rows):
    plan.append([int(i) for i in input().strip().split()]) # build dp array

for i in range(rows):
    for j in range(columns):
        if i == 0 and j == 0:
            plan[i][j] = plan[i][j] # literal edge cases
        elif i == 0:
            plan[i][j] = plan[i][j-1] + plan[i][j]
        elif j == 0:
            plan[i][j] = plan[i-1][j] + plan[i][j]
        else:
            plan[i][j] = min(plan[i][j-1] + plan[i][j], plan[i-1][j] + plan[i][j])
print(plan[-1][-1])