# https://www.geeksforgeeks.org/python-program-to-find-whether-a-no-is-power-of-two/

import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    if n & (n - 1) == 0:
        print("T")
    else:
        print("F")