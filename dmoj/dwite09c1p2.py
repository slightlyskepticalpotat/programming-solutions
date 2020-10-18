import itertools 

for i in range(5):
    print("\n".join(list(sorted(["".join(char) for char in list(itertools.permutations([char for char in input().strip()]))]))))