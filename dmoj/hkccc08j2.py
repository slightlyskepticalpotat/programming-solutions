import sys
input = sys.stdin.readline

def expand(a):
    while len(str(a)) != 1:
        a = sum(map(int, str(a)))
    return a

for i in range(int(input())):
    print(expand(int(input())))