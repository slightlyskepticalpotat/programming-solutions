import itertools

n = [char for char in input().strip()]

candidates = [int("".join(i)) for i in itertools.permutations(n) if int("".join(i)) > int("".join(n))]
if candidates:
    print(min(candidates))
else:
    print(0)