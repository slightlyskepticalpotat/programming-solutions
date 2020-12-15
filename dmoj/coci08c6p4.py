import sys

input = sys.stdin.readline

n, numbers = int(input()), [[int(i) % 3, int(i)] for i in input().split()]
zeros, ones, twos = [number for number in numbers if number[0] == 0], [number for number in numbers if number[0] == 1], [number for number in numbers if number[0] == 2]

if len(ones) != 0 and len(twos) == 0 and len(zeros) == 0:
    print(*[number[1] for number in numbers])
elif len(ones) == 0 and len(twos) != 0 and len(zeros) == 0:
    print(*[number[1] for number in numbers])
elif len(zeros) == 0:
    print("impossible")
elif len(ones) + len(twos) + 1 < len(zeros):
    print("impossible")
else: # try to alternate zeros and nonzeros
    try:
        final1 = [-1] * len(ones) * 2
        final1[::2] = ones
        final1[-1] = [0, zeros[-1][1]] # connect with twos
        zeros.pop()
    except: # there may not be any ones
        pass
    try:
        final2 = [-1] * len(twos) * 2
        final2[::2] = twos
        final = final1 + final2
    except: # there may not be any twos
        pass
    for i in range(1, len(final), 2):
        if final[i] == -1 and len(zeros) > 0:
            final[i] = [0, zeros[-1][1]]
            zeros.pop()
    if len(zeros) > 0:
        final = [[0, zeros[-1][1]]] + final
    print(*[number[1] for number in final if number != -1])