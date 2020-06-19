import sys
input = sys.stdin.readline

a_3pt = int(input())
a_2pt = int(input())
a_1pt = int(input())
b_3pt = int(input())
b_2pt = int(input())
b_1pt = int(input())

a_tot = 3*a_3pt+2*a_2pt+1*a_1pt
b_tot = 3*b_3pt+2*b_2pt+1*b_1pt

if a_tot > b_tot:
    print('A')
elif b_tot > a_tot:
    print('B')
else:
    print('T')