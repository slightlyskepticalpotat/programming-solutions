import itertools

numbers = [int(i) for i in input().split()]
candidates = list(itertools.combinations(numbers, 3))
for candidate in candidates:
    if sum(candidate) == max(numbers):
        print(*sorted(candidate))
        break
