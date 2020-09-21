n, lucky = int(input()), ""

while n: # make a tree diagram
    mod = n % 2
    if mod == 0:
        lucky += "7"
        n -= 1
    else:
        lucky += "4"
    n //= 2
print(lucky[::-1])