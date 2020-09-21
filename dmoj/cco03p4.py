import itertools

n, count = int(input()), 0
constraints = [[int(number) for number in input().split()] for _ in range(int(input()))]
permutations = itertools.permutations([(i + 1) for i in range(n)])

try:
    while True:
        current, flag = next(permutations), True
        for constraint in constraints:
            if current.index(constraint[0]) > current.index(constraint[1]):
                flag = False
                break
        count += int(flag)
except StopIteration:
    print(count)