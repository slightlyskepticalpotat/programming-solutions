for i in range(5):
    number = bin(int(input()))
    if str(number).count("1") % 2 == 1:
        print(1)
    else:
        print(0)