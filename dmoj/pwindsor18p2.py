import sys, math
input = sys.stdin.readline

far = 0
location = []
for i in range(int(input())):
    a, b = map(int, input().split())
    if math.sqrt(a**2 + b**2) > far:
        far = math.sqrt(a**2 + b**2)
        location = [a, b]
print(*location)