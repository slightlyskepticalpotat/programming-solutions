import sys

def palin(x):
    if x == x[::-1]:
        return True
    return False

ree = input().strip()
for i in range(1, len(ree)):
    if len(ree) > 1 and palin(ree[i:]) and palin(ree[:i]):
        print("YES")
        sys.exit()
print("NO")