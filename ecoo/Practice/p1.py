import sys

input = sys.stdin.readline

n = int(input())
if n > 7:
    print("Tootsie Roll!")
elif n < 3:
    print("Rocket!")
else:
    print("NO")
