for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    complement = values[::-1]
    complement = [-complement[i] if i % 2 else complement[i] for i in range(n)]
    print(*complement)
