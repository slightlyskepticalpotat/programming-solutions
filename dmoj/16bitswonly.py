cases = int(input())
for i in range(0,cases):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if a * b == c:
        print('POSSIBLE DOUBLE SIGMA')
    else:
        print('16 BIT S/W ONLY')