import sys

input = sys.stdin.readline

n = int(input())
square = [[int(i) if i.isdigit() else ord(i) - 55 for i in input().strip()] for _ in range(n)]
if all(len(set(i)) == n for i in square):
    square = [list(i) for i in zip(*square[::-1])]
    if all(len(set(i)) == n for i in square):
        square = [list(i) for i in zip(*square[::-1])]
        square = [list(i) for i in zip(*square[::-1])]
        square = [list(i) for i in zip(*square[::-1])]
        if list(sorted(square[0])) == square[0]:
            square = [list(i) for i in zip(*square[::-1])]
            if list(sorted(square[0], reverse = True)) == square[0]:
                print("Reduced")
            else:
                print("Latin")
        else:
            print("Latin")
    else:
        print("No")
else:
    print("No")