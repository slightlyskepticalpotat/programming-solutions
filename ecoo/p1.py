import sys

input = sys.stdin.readline

a, b, c = int(input()), int(input()), int(input())
check = [a + b, a + b * 2, a + b * 3]
for i in range(3):
    if c <= check[i]:
        print(check[i])
        sys.exit()
print("Who knows...")
