names, pile = [char for char in input().strip()] + [char for char in input().strip()], [char for char in input().strip()]
names.sort()
pile.sort()
if names == pile:
    print("YES")
else:
    print("NO")
