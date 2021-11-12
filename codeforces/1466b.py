for _ in range(int(input())):
    n, song, diverse = int(input()), [int(i) for i in input().split()], set()
    for i in range(n):
        if song[i] in diverse:
            diverse.add(song[i] + 1)
        else:
            diverse.add(song[i])
    print(len(diverse))
