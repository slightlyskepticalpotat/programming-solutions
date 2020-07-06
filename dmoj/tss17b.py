# basically https://dmoj.ca/src/2184040

import sys, math
input = sys.stdin.readline

array = [0] * 1414215 # build prefix minimum array
houses, scenarios = map(int, input().split())
for i in range(houses):
    x, y = map(int, input().split())
    array[math.ceil(math.sqrt(x**2 + y**2))] += 1 # mark a house as being destroyed there
for j in range(1414213): # compare arrays from left to right
    array[j+1] += array[j] # propagate the houses

for i in range(scenarios):
    print(array[int(input())])