import sys
input = sys.stdin.readline
elo = int(input())
for i in range(int(input())):
    if abs(elo-int(input())) > 100:
        print("go away! 3:<")
    else:
        print("fite me! >:3")