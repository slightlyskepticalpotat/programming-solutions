import itertools

def power_set(x):
    s = list(x)
    return list(itertools.chain.from_iterable(itertools.combinations(s, i) for i in range(1, len(s)+1))) # get all subsets of len i

diff = 1000000000
ingredients = []
for i in range(int(input())):
    ingredients.append(tuple([int(i) for i in input().split()])) # sourness, bitterness

for thing1 in power_set(ingredients):
    sourness, bitterness = 1, 0
    for thing2 in thing1:
        sourness *= thing2[0]
        bitterness += thing2[1]
    if abs(sourness - bitterness) < diff:
        diff = abs(sourness - bitterness)
print(diff)