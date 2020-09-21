import sys

input = sys.stdin.readline

n, runners = int(input()), {}
for i in range(n):
    runner = input()
    if runner in runners.keys():
        runners[runner] += 1
    else:
        runners[runner] = 1

for i in range(n - 1):
    runner = input()
    runners[runner] -= 1
for runner in runners.keys():
    if runners[runner] == 1:
        print(runner)
        break