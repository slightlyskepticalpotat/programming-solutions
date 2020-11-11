def move(n, start, end, spare):
    if n > 0:
        move(n - 1, start, spare, end) # get all of the discs out of the way except 1
        end[0].append(start[0].pop()) # move the last disc
        print(start[1] + end[1])
        move(n - 1, spare, end, start) # move the remaining discs
    return 0

A, B, C = list(reversed([(i + 1) for i in range(int(input()))])), [], []
move(len(A), [A, "A"], [C, "C"], [B, "B"]) # [discs, name]