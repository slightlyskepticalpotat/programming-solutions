import math

def base(x, base):
    result = []
    while x:
        ree = divmod(x, base) # faster
        result.append(ree[1])
        x = ree[0]
    return result == result[::-1]

n = int(input())

for i in range(2, math.ceil(math.sqrt(n))):
    if base(n, i):
        print(i)
for i in range(math.ceil(math.sqrt(n)), 0, -1): # increasing order
    ree = divmod(n - i, i)
    if not ree[1] and ree[0] > i:
        print(ree[0])