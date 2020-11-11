def check(x):
    if x == sum([int(char) ** 3 for char in str(x)]):
        return True
    return False

start, stop = map(int, input().split())
true = []

for i in range(start, stop + 1):
    if check(i):
        true.append(str(i))
print("\n".join(true))