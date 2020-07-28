import math

first = [math.sqrt(int(i)) // 1 for i in input().split()]
second = [math.sqrt(int(i)) // 1 for i in input().split()]
if first == second:
    print("Dull")
else:
    print("Colourful")