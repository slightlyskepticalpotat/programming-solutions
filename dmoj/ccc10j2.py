a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

x = (s // (a + b)) * (a - b) + min(a, s - (s // (a + b)) * (a + b)) # whole cycles, a part cycle
y = (s // (c + d)) * (c - d) + min(c, s - (s // (c + d)) * (c + d))
if x > y:
    print("Nikky")
elif y > x:
    print("Byron")
else:
    print("Tied")