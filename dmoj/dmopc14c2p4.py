import sys
input = sys.stdin.readline

tree_count = int(input())
trees = []
tree_masses = []
sum = 0
for i in range(tree_count):
    trees.append(int(input()))
for i in range(0, tree_count):
    sum += trees[i]
    tree_masses.append(sum)
query_count = int(input())
for i in range(query_count):
    query = [int(i) for i in input().strip().split()]
    sys.stdout.write(
        str(tree_masses[query[1]] - tree_masses[query[0]] + trees[query[0]]) + "\n")