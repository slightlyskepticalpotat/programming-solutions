import math, sys

input = sys.stdin.readline

n = int(input())
x_cords = [float(i) for i in input().split()]
y_cords = [float(i) for i in input().split()]
print(math.sqrt(sum([(x_cords[i] - y_cords[i]) ** 2 for i in range(n)])))