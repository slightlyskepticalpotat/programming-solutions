thing = int("100000000000000000000", 2)
for _ in range(int(input())):
    first = int(input().strip(), 16)
    if first & thing: # bitwise black magic; & checks if 20th bit is already 1 and therefore affected
        print(hex(first & (~thing))[2:].zfill(8).upper(), hex(first)[2:].zfill(8).upper()) # basically negates it by flipping it
    else:
        print(hex(first)[2:].zfill(8).upper())