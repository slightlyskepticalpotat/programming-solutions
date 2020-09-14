import sys

input = sys.stdin.readline

def toposort():
    global stack
    stack = []
    for i in range(6, 0, -1):
        if not visited[i]:
            toposort_recurse(i)
    return stack

def toposort_recurse(x):
    visited[x] = True
    for peer in tasks[x + 1]: # 1-indexed
        if not visited[peer - 1]:
            toposort_recurse(peer - 1)
    stack.insert(0, x + 1)

def toposort_validate(x):
    for i in range(7):
        for peer in tasks[i + 1]:
            if x.index(peer) < x.index(i + 1): # check if any child node occur before parent nodes
                return False
    return True


tasks = {1: [4, 7], 2: [1], 3: [4, 5], 4: [], 5: [], 6: [], 7: []}
visited = [False, False, False, False, False, False, False]

while True:
    a, b = int(input()), int(input())
    if a ^ b == 0:
        break
    else:
        tasks[a].append(b)

tasks = {i + 1: sorted(tasks[i + 1], reverse = True) for i in range(7)} # lowest first
order = toposort()

if toposort_validate(order):
    print(*order)
else:
    print("Cannot complete these tasks. Going to bed.")