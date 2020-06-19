import sys
input = sys.stdin.readline
a, b, c, d = map(int, input().strip().split())
carbon = a + b + c + 1
hydrogen = d
if carbon*4 - 2*a - 2*b*1/2 - 3*c*1/2 - d == 0:
    print("C"+str(carbon)+"H"+str(hydrogen))
else:
    print("invalid")