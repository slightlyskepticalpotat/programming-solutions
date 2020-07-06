import sys
input = sys.stdin.readline

def path(x, y): # if x < y and y < z, x < z, so we bfs
    queue = [x]
    searched = [False] * (people + 1)
    while queue:
        searching = queue.pop()
        if searching == y:
            return True
        for i in heights[searching]:
            if searched[i] == False:
                queue.append(i)
        searched[searching] = True
    return False

people, comparisons = map(int, input().split())
heights = [[] for i in range(people + 1)] # faster
for i in range(comparisons):
    taller, shorter = map(int, input().split())
    heights[taller].append(shorter)
p, q = map(int, input().split())

if path(p, q):
    print("yes")
elif path(q, p):
    print("no")
else:
    print("unknown")