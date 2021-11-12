for _ in range(int(input())):
    n, q = map(int, input().split())
    string = input().strip()
    for i in range(q):
        l, r = map(int, input().split())
        target, flag = string[l - 1:r], False
        for j in range(l - 1):
            if string[j] == target[0]:
                flag = True
        for j in range(r, n):
            if string[j] == target[-1]:
                flag = True
        if flag:
            print("YES")
        else:
            print("NO")
