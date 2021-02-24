import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    initial, desired, colours, paint_this, final, flag = [int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()], -1, [-1 for i in range(m)], False
    changes = {colour: [] for colour in set(desired) | set(colours)}
    for i in range(n):
        if initial[i] != desired[i]:
            changes[desired[i]].append(i)
    if colours[-1] in changes and len(changes[colours[-1]]) > 0: # find something everyone but the last painter can paint
        paint_this = changes[colours[-1]].pop()
    else:
        for i in range(n):
            if desired[i] == colours[-1]:
                paint_this = i
    if paint_this == -1:
        print("NO")
        flag = True
    final[-1] = paint_this
    for i in range(m - 1):
        if len(changes[colours[i]]) == 0:
            final[i] = paint_this
        else:
            final[i] = changes[colours[i]].pop()
    for key in changes:
        if len(changes[key]) and not flag:
            print("NO")
            flag = True
    if not flag:
        print("YES")
        print(*[final[i] + 1 for i in range(m)])
