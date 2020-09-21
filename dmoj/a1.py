import sys

input = sys.stdin.readline

for i in range(int(input())):
    m, word = input().strip().split(" ", 1)
    print(f"{i + 1} {word[:int(m) - 1] + word[int(m):]}")