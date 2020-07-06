import sys, bisect
input = sys.stdin.readline

freq = {}
favourites_count = int(input())
favourites = sorted([int(i) for i in input().split()])
for thing in favourites:
    if not thing in freq.keys():
        freq[thing] = 0
    freq[thing]+=1
numbers_count = int(input())
numbers = [int(input()) for _ in range(numbers_count)]

for thing in numbers:
    lowest = favourites[bisect.bisect_left(favourites, thing)]
    print(lowest, freq[lowest])