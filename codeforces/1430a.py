for _ in range(int(input())):
    n = int(input())
    try:
        for i in range(334):
            for j in range(201):
                e = n - (3 * i + 5 * j)
                if not e % 7 and e >= 0 and 3 * i + 5 * j + e == n:
                    print(i, j, e // 7)
                    raise

        print(-1)
    except:
        pass
