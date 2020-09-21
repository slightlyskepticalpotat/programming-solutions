import statistics, sys

input = sys.stdin.readline

n, integers = int(input()), [int(i) for i in input().split()]
average = statistics.mean(integers)
if len([i for i in integers if i > average]) > len(integers) / 2:
    print("Winnie should take the risk")
else:
    print("That's too risky")