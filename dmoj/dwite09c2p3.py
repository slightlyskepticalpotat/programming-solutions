for i in range(5):
    blacklist = str(input())
    for j in range(0, 16):
        candidate = str(bin(j)[2:].zfill(4))
        if blacklist not in candidate:
            print(candidate)