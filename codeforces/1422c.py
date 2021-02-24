n, mod, tot, loc = input().strip(), 10 ** 9 + 7, 0, 0
for i, c in enumerate(n[::-1]): # i, digit
    p = len(n) - 1 - i
    tot = (tot + p * (p + 1) // 2 * int(c) * pow(10, i, mod) + loc * int(c)) % mod # left removed and right removed, respectively
    loc = (loc + (i + 1) * pow(10, i, mod)) % mod # update right removed
print(tot % mod)
