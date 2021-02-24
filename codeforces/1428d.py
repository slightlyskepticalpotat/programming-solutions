n, values, row, one, ans, flag, two = int(input()), [int(i) for i in input().split()], 1, [], [], True, []
for i in range(n - 1, -1, -1):
    if values[i] == 0:
        pass
    elif values[i] == 1:
        one.append([row, i])
        ans.append([row, i])
        row += 1
    elif values[i] == 2:
        if not one:
            flag = False
            break
        last = one.pop()
        ans.append([last[0], i])
        two = [last[0], i]
    elif values[i] == 3:
        if not two:
            if not one:
                flag = False
                break
            else:
                two = one.pop()
        ans.append([row, i])
        ans.append([row, two[1]])
        two = [row, i]
        row += 1
if not flag:
    print(-1)
else:
    print(len(ans))
    for row in ans:
        print(n - row[0] + 1, row[1] + 1)
