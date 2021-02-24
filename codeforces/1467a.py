for _ in range(int(input())):
    n = int(input())
    panels = [0 for _ in range(n)]
    pause = min(len(panels), 1)
    for i in range(n):
        if i <= pause:
            panels[i] = (9 - i) % 10
        else:
            panels[i] = (i - pause - 2) % 10
    print("".join([str(i) for i in panels]))
