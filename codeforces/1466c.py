for _ in range(int(input())):
    poetry = input().strip() + "!"
    replace = [0 for _ in range(len(poetry))]
    for i in range(1, len(poetry)):
        if poetry[i] == poetry[i - 1] and not replace[i - 1]:
            replace[i] = 1
        if i > 1 and poetry[i] == poetry[i - 2] and not replace[i - 2]:
            replace[i] = 1
    print(sum(replace))
