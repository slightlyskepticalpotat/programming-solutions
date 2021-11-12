import sys 

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    low, high = -1, -1
    if a < c:
        low = 1
    high_donuts = 10 ** 9 - (10 ** 9) % b
    if (high_donuts // b) * c < high_donuts * a:
        high = high_donuts 
    print(low, high)