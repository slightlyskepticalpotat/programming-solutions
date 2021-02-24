import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, string = int(input()), input().strip() + " "
    far_left, far_right = [i for i in range(n + 1)], [i for i in range(n + 1)]
    for i in range(1, n + 1):
        if string[i - 1] == "R": # stopped
            far_left[i] = i
        elif i == 1 or string[i - 2] != "R": # stopped
            far_left[i] = i - 1
        else: # can extend
            far_left[i] = far_left[i - 2]
    for i in range(n - 1, -1, -1): # same process backwards
        if string[i] == "L":
            far_right[i] = i
        elif i == n - 1 or string[i + 1] != "L":
            far_right[i] = i + 1
        else:
            far_right[i] = far_right[i + 2]
    print(*[far_right[i] - far_left[i] + 1 for i in range(n + 1)])
