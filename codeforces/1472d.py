import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, bob, alice = int(input()), 0, 0
    elements = [int(i) for i in input().split()]
    elements.sort()
    for i in range(n):
        cache = elements.pop()
        if not i % 2:
            if not cache % 2:
                alice += cache
        else:
            if cache % 2:
                bob += cache
    if alice > bob:
        print("Alice")
    elif bob > alice:
        print("Bob")
    else:
        print("Tie")
