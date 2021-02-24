n, balance = int(input()), {25: 0, 50: 0, 100: 0}
queue, flag = [int(i) for i in input().split()], True
for i in range(n):
    if queue[i] == 25:
        balance[25] += 1
    elif queue[i] == 50:
        if balance[25]:
            balance[25] -= 1
            balance[50] += 1
        else:
            flag = False
    elif queue[i] == 100:
        if balance[25] and balance[50]:
            balance[25] -= 1
            balance[50] -= 1
            balance[100] += 1
        elif balance[25] >= 3:
            balance[25] -= 3
            balance[100] += 1
        else:
            flag = False
if flag:
    print("YES")
else:
    print("NO")
