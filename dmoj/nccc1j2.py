def palin(x):
    if x == x[::-1]:
        return True
    return False

s, flag = input().strip(), True
substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

for substring in substrings:
    if palin(substring):
        if len(substring) % 2 == 0:
            flag = False
if flag:
    print("Odd")
else:
    print("Even")