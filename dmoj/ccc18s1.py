import sys
input = sys.stdin.readline
count = int(input())
loc = []
bounds = []
smallest = 10000000000000000000

for i in range(count):
    loc.append(int(input()))
loc = sorted(loc)

for i in range(1, count):
    bounds.append((loc[i]-loc[i-1])/2)

for i in range(1, len(bounds)):
    if bounds[i]+bounds[i-1] < smallest:
        smallest = bounds[i]+bounds[i-1]

print(smallest)