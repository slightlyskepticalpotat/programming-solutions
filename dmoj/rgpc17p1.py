import sys, math
input = sys.stdin.readline

sequence, size = map(int, input().split())
positions, combos = [], [1]
for i in range(sequence):
    positions.append([int(i) for i in input().split()])

for i in range(0, sequence - 1):
    if math.sqrt((positions[i+1][0] - positions[i][0])**2 + (positions[i+1][1] - positions[i][1])**2) <= size:
        combos.append(combos[-1] + 1)
    else:
        combos.append(0)
print(max(combos))