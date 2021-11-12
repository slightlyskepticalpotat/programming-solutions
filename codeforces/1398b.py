import itertools, sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    segs = ["".join(i) for _, i in itertools.groupby(s)]
    segs, alice = sorted([i for i in segs if not "0" in i]), 0
    while segs:
        alice += len(segs.pop())
        if not segs:
            break
        segs.pop()
    print(alice)
