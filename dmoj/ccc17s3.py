import sys, collections
input = sys.stdin.readline

number, count = int(input()), {i: 0 for i in range(1, 2001)}
boards = [int(i) for i in input().strip().split()]
length, fences = 0, 0
for thing in boards:
    count[thing] += 1

for i in range(2, 4001):
    candidate = 0
    for j in range(1, i):
        if j in count and i - j in count: # work backwards
            candidate += min(count[j], count[i - j])
    if candidate > length:
        length = candidate
        fences = 1
    elif candidate == length:
        fences += 1
print(length // 2, fences) # overcount