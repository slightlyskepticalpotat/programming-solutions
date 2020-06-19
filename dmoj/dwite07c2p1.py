import sys

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, (x // 2)+1):
        if x % i == 0:
            return False
    return True

for i in range(0, 5):
    flag = 0
    number = int(sys.stdin.readline())
    if is_prime(number):
        print("not")
    else:
        for i in range(1, number):
            if number % i == 0:
                z = int(number/i)
                if is_prime(z) and is_prime(i):
                    flag = 1
                    print("semiprime")
                    break
        if flag == 0:
            print("not")