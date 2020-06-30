import sys
input = sys.stdin.readline

def factors(x):
    factors = set()
    for i in range(1, x):
        if x % i == 0:
            factors.add(i)
    return sum(factors)

for i in range(int(input())):
    number = int(input())
    ree = factors(number)
    if ree == number:
        print(number, " is a perfect number.")
    elif ree < number:
        print(number, " is a deficient number.")
    elif ree > number:
        print(number, " is an abundant number.")