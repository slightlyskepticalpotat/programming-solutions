import math
a = int(input())
b = int(input())+1
cool = 0
for i in range(a, b):
    if math.sqrt(i) == int(math.sqrt(i)) and round(i ** (1/3))**3 == i:
        cool+=1
print(cool)