import sys, itertools
input = sys.stdin.readline

for i in range(int(input())):
    n, k = map(int, input().strip().split())
    ree = "1" * k + "0" * (n - k)
    print("The bit patterns are")
    while True:
        print(ree)
        insert = ree.rfind("10")
        ree = ree[:insert] + "01" + ree[insert + 2:][::-1] # reverse the last 10, reverse that, reverse the remainder
        if len(ree) > n:
            break
    print("")