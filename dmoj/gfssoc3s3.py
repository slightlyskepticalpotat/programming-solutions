n = int(input())

if n == 1:
    print(9)
elif n > 16:
    print(999999998)
else:
    if n % 2 == 0:
        pre_mod = "1" + "9"*((n-1)//2) + "8"

    else:
        pre_mod = "1" + "0" + "9"*((n-2)//2) + "8"
    print(pre_mod)