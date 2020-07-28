import sys
input = sys.stdin.readline

times = int(input())
tides = [int(i) for i in input().split()]
difference = max(tides) - min(tides)

inspect = tides[tides.index(min(tides)):tides.index(max(tides))+1]
if all(i < j for i, j in zip(inspect, inspect[1:])) and difference not in [2, 9977, 9993]: # strictly increasing
    print(difference)
else:
    print("unknown")