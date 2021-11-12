import math, sys

input = sys.stdin.readline

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if not x % i:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print("FastestFinger")
    elif n == 2:
        print("Ashishgup")
    elif math.log2(n) == math.log2(n) // 1:
        print("FastestFinger")
    elif not n % 2 and is_prime(n // 2):
        print("FastestFinger")
    else:
        print("Ashishgup")