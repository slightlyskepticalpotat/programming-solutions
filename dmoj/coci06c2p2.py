a, b, c = sorted(map(int, input().split()))
order = list(input().lower())
for thing in order:
    exec('''print({order}, end=" ")'''.format(order=thing))