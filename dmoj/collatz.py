n, i = int(input()), 0
while True:
    if n == 1:
        print(i)
        break
    elif n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    i += 1