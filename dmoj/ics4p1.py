import itertools
word = sorted([''.join(thing) for thing in itertools.permutations(input().strip())])
for thing in word:
    print(thing)