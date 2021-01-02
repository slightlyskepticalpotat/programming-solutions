import statistics, sys

input = sys.stdin.readline

for _ in range(5):
    pennies = [int(input()) for _ in range(int(input()))]
    average = statistics.mean(pennies)
    moves = [abs(penny - average) for penny in pennies]
    print(sum(moves) // 2)