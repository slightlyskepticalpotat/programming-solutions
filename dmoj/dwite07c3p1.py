def unique(x):
    factors = []
    while x != 1:
        for i in range(1, x + 1):
            if x % i == 0:
                x //= i
                factors.append(i)
    return len(set(factors)) - 1

for i in range(5):
    if unique(int(input())) == 3:
        print("valid")
    else:
        print("not")