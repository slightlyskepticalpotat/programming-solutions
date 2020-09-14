import sys

input = sys.stdin.readline
sys.setrecursionlimit(2147483647)

def dfs(x):
    visited.add(x)
    for peer in talkers[x]:
        if peer in visited or dfs(peer):
            return True
    visited.remove(x)

students, connections = int(input()), int(input())
talkers, visited = {i + 1: [] for i in range(students)}, set()

for i in range(connections):
    a, b = map(int, input().split())
    talkers[a].append(b)

for student in talkers.keys():
    if talkers[student] != []:
        if dfs(talkers[student][0]):
            print("N")
            sys.exit(0)
print("Y")