import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n % 2:
        print("Bob")
    else:
        if math.log2(n) == math.log2(n) // 1:
            if math.log2(n) % 2:
                print("Bob")
            else:
                print("Alice")
        else:
            print("Alice")
