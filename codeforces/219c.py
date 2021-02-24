n, k = map(int, input().split())
if k == 2:
    ab, ba = "AB" * (n // 2) + "A" * (n % 2), "BA" * (n // 2) + "B" * (n % 2)
    ab_c, ba_c = 0, 0
    old = input().strip()
    for i in range(n):
        ab_c += (old[i] != ab[i])
        ba_c += (old[i] != ba[i])
    if ab_c < ba_c:
        print(ab_c)
        print(ab)
    else:
        print(ba_c)
        print(ba)
else:
    old, req, avail = [char for char in input().strip()], 0, "ABCDEFGHIJKLMNOPQRSTUVWXYZA"
    for i in range(1, n):
        if old[i] == old[i - 1]:
            old[i] = avail[(avail.find(old[i - 1]) + 1) % k]
            if i != n - 1 and old[i] == old[i + 1]:
                old[i] = avail[(avail.find(old[i]) + 1) % k]
            req += 1
    print(req)
    print("".join(old))
