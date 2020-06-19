# https://en.wikipedia.org/wiki/Gauss_circle_problem
import math, sys
input = sys.stdin.readline

while True:
    radius = int(input())
    if radius == 0:
        break
    else:
        pennies = 0
        radius_squared = radius*radius
        for i in range(radius+1):
            pennies+=int(math.sqrt(radius_squared-i*i))
        print(pennies*4+1)