for _ in range(int(input())):
    n, string, flag = int(input()), input().strip(), False
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if string[:i] + string[j:] == "2020":
                flag = True
    if string == "2020" or flag:
        print("YES")
    else:
        print("NO")
