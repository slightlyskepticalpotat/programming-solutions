import sys

input = sys.stdin.readline

for i in range(int(input())):
    ecoo = input().strip()
    print("Educational " * (ecoo.count("E")), end = "")
    print("Computing ", end = "")
    print("Organization of Ontario " * (ecoo.count("O") // 2))