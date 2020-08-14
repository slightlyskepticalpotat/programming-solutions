sequence = [int(i) for i in input().strip().split()]

while sequence != [1, 2, 3, 4, 5]:
    if sequence[0] > sequence[1]:
        sequence[0], sequence[1] = sequence[1], sequence[0]
        print(*sequence)
    if sequence[1] > sequence[2]:
        sequence[1], sequence[2] = sequence[2], sequence[1]
        print(*sequence)
    if sequence[2] > sequence[3]:
        sequence[2], sequence[3] = sequence[3], sequence[2]
        print(*sequence)
    if sequence[3] > sequence[4]:
        sequence[3], sequence[4] = sequence[4], sequence[3]
        print(*sequence)