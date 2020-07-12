import sys
input = sys.stdin.readline

for i in range(int(input())):
    text = [char for char in input().split()]
    nouns = 0
    for thing in text:
        if thing != thing.lower():
            nouns += 1
    print(nouns)