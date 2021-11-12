for _ in range(int(input())):
    s, ans = input().strip(), ""
    for i in range(len(s)):
        if not i % 2:
            if s[i] != "a":
                ans += "a"
            else:
                ans += "b"
        else:
            if s[i] != "z":
                ans += "z"
            else:
                ans += "y"
    print(ans)
