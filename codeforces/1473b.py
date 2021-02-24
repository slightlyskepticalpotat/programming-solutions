for _ in range(int(input())):
    s, t, lcm, lcm_len = input().strip(), input().strip(), "", float("inf")
    for i in range(1, 401):
        if s * i == (len(s) * i) // len(t) * t and len(s) * i < lcm_len:
            lcm_len = len(s) * i
            lcm = s * i
    if lcm:
        print(lcm)
    else:
        print(-1)
