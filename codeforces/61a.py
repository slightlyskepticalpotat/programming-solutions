a, b = str(input()), str(input())
l = len(a)
a, b = int(a, 2), int(b, 2)
print(bin(a ^ b)[2:].zfill(l))
