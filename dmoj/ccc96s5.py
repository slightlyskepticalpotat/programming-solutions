import sys

input = sys.stdin.readline

def d(x, y):
    if y >= x and seq2[y] >= seq1[x]:
        return y - x
    else:
        return 0

for _ in range(int(input())):
    l = int(input())
    seq1 = [int(i) for i in input().strip().split()]
    seq2 = [int(i) for i in input().strip().split()]
    possible_d = []
    for i in range(l):
        for j in range(l):
            possible_d.append(d(i, j))
    print(f"The maximum distance is {max(possible_d)}")