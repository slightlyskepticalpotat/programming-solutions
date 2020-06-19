# https://dmoj.ca/problem/ccc14s2
import sys
input = sys.stdin.readline
people = input()
partner1 = input().split()
partner2 = input().split()

try:
    for i in range(len(partner1)):
        if partner1[i] == partner2[i] or partner1.index(partner2[i]) != partner2.index(partner1[i]):
            print('bad')
            raise

    print('good')
except:
    pass