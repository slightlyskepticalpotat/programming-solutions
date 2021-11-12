import math

def prod(x):
    ans = 1
    for i in x:
        ans = (ans * i) % n
    return ans

n, values = int(input()), []
for i in range(1, n):
    if math.gcd(n, i) == 1: # add if coprime
        values.append(i)
if prod(values) != 1:
    values.remove(prod(values))
print(len(values))
print(*values)
