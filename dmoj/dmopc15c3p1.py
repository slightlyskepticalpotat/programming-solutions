a = int(input())
b = int(input())
c = int(input())
d = int(input())

if max(a, b) > min(c, d) and min(a, b) < max(c, d):
    print("YES")
else:
    print("NO")