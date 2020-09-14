# format is friend: [invited friends]

import sys
from collections import deque

input = sys.stdin.readline

def powerset(x): # generator
    if len(x) <= 1:
        yield x
        yield []
    else:
        for thing in powerset(x[1:]):
            yield [x[0]] + thing
            yield thing

n, removal_sets = int(input()), []
friends = {(i + 1): [] for i in range(n)}
for i in range(1, n):
    friends[int(input())].append(i)

for i in range(n):
    for j in range(i + 1, n): # different sets of people we can remove
        for thing in powerset(list(friends.keys())):
            removal_set = set()

            for friend in thing:
                queue = deque([friend])
                removal_set.add(friend)
                while queue: # we bfs their friends
                    searching = queue.popleft()
                    removal_set.add(searching)
                    for thing in friends[searching]:
                        if thing not in removal_set:
                            queue.append(thing)

            if list(removal_set) not in removal_sets:
                removal_sets.append(list(removal_set))

removal_sets.remove([1]) # mark can't be removed
print(len(removal_sets))