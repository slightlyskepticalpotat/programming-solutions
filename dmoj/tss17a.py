for i in range(int(input())):
    one, two, three = input().split()
    if one == two:
        print(one)
    elif one == three:
        print(one)
    elif two == three:
        print(two)
    else:
        print("???")