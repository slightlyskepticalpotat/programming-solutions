for _ in range(int(input())):
    n, cords, areas = int(input()), [int(i) for i in input().split()], set()
    for cord1 in cords:
        for cord2 in cords:
            areas.add(abs(cord1 - cord2))
    areas.remove(0)
    print(len(areas))
