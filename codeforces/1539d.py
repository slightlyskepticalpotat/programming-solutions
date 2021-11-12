import sys

input = sys.stdin.readline

prod, ones, twos = sorted([[int(i) for i in input().split()] for j in range(int(input()))], key = lambda x: x[1]), 0, 0 # required, discount
for i in range(len(prod)): # initially buy at full price
    twos += prod[i][0]

for i in range(len(prod) - 1, -1, -1): # try to apply discount
    left = max(twos - prod[i][1], 0) # discount eligibility
    twos, ones = twos - min(left, prod[i][0]), ones + min(left, prod[i][0])
print(twos * 2 + ones)
