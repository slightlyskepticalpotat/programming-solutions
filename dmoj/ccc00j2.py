import sys,copy
allowed_chars = set('01869')
allowed_chars2 = set('018')
allowed_chars3 = set('69')

input = sys.stdin.readline
low = int(input())
hi = int(input())
num = 0


for i in range(low,hi):
    ree = str(i)
    i2 = 'ree'
    
    if set(ree).issubset(allowed_chars):
        i2 = copy.copy(ree)
        i2 = i2.replace('6','7')
        i2 = i2.replace('9','6')
        i2 = i2.replace('7','9')
        if i2[::-1] == ree:
            num+=1
print(num)