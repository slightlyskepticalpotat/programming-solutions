import sys, math
input = sys.stdin.readline

def xgcd(x: int, y: int): # type hints
    x0, x1, y0, y1 = 0, 1, 1, 0
    while x != 0:
        (a, x), y = divmod(y, x), x
        y0, y1 = y1, y0 - a * y1
        x0, x1 = x1, x0 - a * x1
    return y

def largest_prime(x):
    factors = []
    while x % 2 == 0:
        factors.append(2)
        x = x/2
    for i in range(3, int(math.sqrt(x))+1,2):
        while x % i == 0:
            factors.append(int(i))
            x = x/i
    if x > 2:
        factors.append(int(x))
    return(max(factors))

n = int(input())
numbers = [int(i) for i in input().strip().split()]

gcd = xgcd(numbers[0], numbers[1])
for i in range(1, n):
    gcd = xgcd(gcd, numbers[i])
try:
    print(largest_prime(gcd))
except:
    print("DNE")