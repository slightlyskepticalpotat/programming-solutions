import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, array, locks = int(input()), [int(i) for i in input().split()], [int(i) for i in input().split()]
    unlocked = list(sorted([array[i] for i in range(n) if not locks[i]]))
    print(*[unlocked.pop() if not locks[i] else array[i] for i in range(n)])
