# must be at least 1 bit different, we set it as leftmost 0

l, r = map(int, input().split())
target, final = l ^ r, 1
while target:
    target >>= 1
    final <<= 1
print(final - 1)
