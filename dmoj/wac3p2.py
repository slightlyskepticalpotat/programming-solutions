import sys
input = sys.stdin.readline

for _ in range(int(input())):
    hours = int(input())
    time = hours // 3
    if hours % 3 == 0:
        print(int(time ** 3))
    elif hours % 3 == 1:
        print(int(time * time * (time + 1)))
    elif hours % 3 == 2:
        print(int(time * (time + 1) * (time + 1)))