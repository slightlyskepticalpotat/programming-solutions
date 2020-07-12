matches, a, b = map(int, input().split())
for i in range(matches):
    if int(input())**2 <= a**2 + b**2:
        print("DA")
    else:
        print("NE")