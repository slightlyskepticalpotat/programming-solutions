import itertools

def power_set(x):
    s = list(x)
    return list(itertools.chain.from_iterable(itertools.combinations(s, i) for i in range(1, len(s)+1)))

for _ in range(int(input())):
    n, base, works = int(input()), [i for i in range(10)], []
    if n > 45:
        print(-1)
    else:
        for subset in power_set(base):
            if sum(subset) == n:
                works.append(int("".join([str(i) for i in subset])))
        print(min(works))
