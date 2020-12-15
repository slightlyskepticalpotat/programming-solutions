import itertools, sys

input = sys.stdin.readline

def valid(colouring):
    for i in range(n):
        for neighbour in t_shirt[i]:
            if colouring[neighbour] == colouring[i]:
                return False
    return True

for _ in range(5):
    n, answer = int(input()), 0
    t_shirt = [[] for _ in range(n)] # adjacency list
    for _ in range(n):
        a, b = map(int, input().split())
        if a != b:
            t_shirt[a - 1].append(b - 1)
            t_shirt[b - 1].append(a - 1)
    try:
        for i in range(1, 5): # brute force number of colourings
            for colouring in itertools.product(list(range(i)), repeat = n): # cartesian product, essentially for loops https://stackoverflow.com/questions/52194927/how-to-generate-all-possible-arrangements-of-numbers-from-a-list-in-python
                if valid(colouring):
                    print(i)
                    raise
        print(answer)
    except:
        pass