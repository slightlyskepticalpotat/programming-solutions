import math, copy

low = int(input())
high = int(input())
rsa = 0

for i in range(low-1,high+1):
    divisors = 0
    number = copy.copy(i)
    for j in range(1,number+1):
        if number % j == 0:
            divisors += 1
    if divisors == 4:
        rsa += 1

print('The number of RSA numbers between %s and %s is %s' % (low,high,rsa))