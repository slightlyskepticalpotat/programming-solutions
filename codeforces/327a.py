n, paper = int(input()), [int(i) for i in input().split()]
original, best = paper.count(1), -float("inf")
for i in range(n):
    for j in range(i, n):
        segment = paper[i:j + 1]
        if segment.count(0) - segment.count(1) > best:
            best = segment.count(0) - segment.count(1)
print(original + best)
