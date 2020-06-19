import sys, math
input = sys.stdin.readline
cases = int(input())

def is_prime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

for i in range(0, cases):
    avg = int(input())*2
    for i in range(2, int(avg)):
        a = int(i)
        b = int(avg - i)
        if is_prime(a) == True:
            if is_prime(b) == True:
                print(a, b)
                break