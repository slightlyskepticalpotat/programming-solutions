import copy
n = int(input())
k = int(input())
number = copy.copy(n)

for i in range(0,k):
    number = number + n*10**k
    k-=1
print(number)