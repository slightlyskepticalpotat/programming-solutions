import sys
input = sys.stdin.readline

for i in range(5):
    letters = [char for char in input().strip()]
    for thing in letters:
        if letters.count(thing) == 1:
            print(thing)
            break