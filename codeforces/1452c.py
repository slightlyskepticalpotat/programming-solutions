for _ in range(int(input())):
    t = input().strip()
    sq, rd, rbs = 0, 0, 0
    for i in range(len(t)):
        if t[i] == "(":
            rd += 1
        elif t[i] == "[":
            sq += 1
        elif t[i] == ")" and rd > 0:
            rbs += 1
            rd -= 1
        elif t[i] == "]" and sq > 0:
            rbs += 1
            sq -= 1
    print(rbs)
