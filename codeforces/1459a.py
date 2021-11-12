import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, prob = int(input()), 0
    red = [int(i) for i in input().strip()]
    blue = [int(i) for i in input().strip()]
    for i in range(n):
        if red[i] > blue[i]:
            prob += 1
        elif blue[i] > red[i]:
            prob -= 1
    if prob > 0:
        print("RED")
    elif prob < 0:
        print("BLUE")
    else:
        print("EQUAL")
