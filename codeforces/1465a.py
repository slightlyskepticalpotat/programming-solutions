for _ in range(int(input())):
    n, c = int(input()), 0
    string = input().strip()[::-1]
    for char in string:
        if char == ")":
            c += 1
        else:
            break
    if c > len(string) - c:
        print("YES")
    else:
        print("NO")
