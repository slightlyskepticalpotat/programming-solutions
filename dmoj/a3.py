for t in range(int(input())):
    k = int(input())
    print(min([n for n in [k // 1000 * 1000 + 192, k // 1000 * 1000 + 442, k // 1000 * 1000 + 692, k // 1000 * 1000 + 942] if n > k]))