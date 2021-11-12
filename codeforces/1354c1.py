import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input()) * 2
    if n == 4: # square
        print(1)
    else:
        large_angle = (((n - 2) * 180) / n) / 2
        small_angle = 180 - 2 * large_angle
        alt = math.sin(math.radians(large_angle)) / math.sin(math.radians(small_angle)) # law of sines
        print(math.sqrt(alt ** 2 - 0.5 ** 2) * 2)