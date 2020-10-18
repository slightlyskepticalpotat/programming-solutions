import itertools

def powerset(x):
    if len(x) <= 1:
        yield x
        yield []
    else:
        for thing in powerset(x[1:]):
            yield [x[0]] + thing
            yield thing

n = int(input())
integers = [int(i) for i in input().strip().split()]
total, minimum = sum(integers), float("inf")

for group in list(powerset(integers)):
    candidate = abs(sum(group) - (total - sum(group)))
    if candidate < minimum:
        minimum = candidate
print(minimum)