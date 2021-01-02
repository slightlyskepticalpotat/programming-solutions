# row, column, top left is 0, 0

def construct_fractal(top_left, top_right, bottom_left, bottom_right, lvl):
    if lvl:
        lvl -= 1
        for i in range(top_left[0] + 3 ** lvl, top_left[0] + 3 ** lvl + 3 ** lvl):
            for j in range(top_left[1] + 3 ** lvl, top_left[1] + 3 ** lvl + 3 ** lvl):
                fractal[i][j] = " "
        if lvl:
            construct_fractal(top_left, (top_right[0], top_right[1] - 3 ** lvl - 3 ** lvl), (bottom_left[0] - 3 ** lvl - 3 ** lvl, bottom_left[1]), (bottom_right[0] - 3 ** lvl - 3 ** lvl, bottom_right[1] - 3 ** lvl - 3 ** lvl), lvl)
            construct_fractal((top_left[0], top_left[1] + 3 ** lvl), (top_right[0], top_right[1] - 3 ** lvl), (bottom_left[0] - 3 ** lvl - 3 ** lvl, bottom_left[1] + 3 ** lvl), (bottom_right[0] - 3 ** lvl - 3 ** lvl, bottom_right[1] - 3 ** lvl), lvl)
            construct_fractal((top_left[0], top_left[1] + 3 ** lvl + 3 ** lvl), top_right, (bottom_left[0] - 3 ** lvl - 3 ** lvl, bottom_left[1] + 3 ** lvl + 3 ** lvl), (bottom_right[0] - 3 ** lvl - 3 ** lvl, bottom_right[1]), lvl)
            construct_fractal((top_left[0] + 3 ** lvl, top_left[1]), (top_right[0] + 3 ** lvl, top_right[1] - 3 ** lvl), (bottom_left[0] - 3 ** lvl, bottom_right[1]), (bottom_right[0] - 3 ** lvl, bottom_right[1] - 3 ** lvl - 3 ** lvl), lvl)
            construct_fractal((top_left[0] + 3 ** lvl, top_left[1] + 3 ** lvl + 3 ** lvl), (top_right[0] + 3 ** lvl, top_right[1]), (bottom_left[0] - 3 ** lvl, bottom_left[1] + 3 ** lvl + 3 ** lvl), (bottom_right[0] - 3 ** lvl, bottom_right[1]), lvl)
            construct_fractal((top_left[0] + 3 ** lvl + 3 ** lvl, top_left[1]), (top_right[0] + 3 ** lvl + 3 ** lvl, top_right[1] - 3 ** lvl - 3 ** lvl), bottom_left, (bottom_right[0], bottom_right[1] - 3 ** lvl - 3 ** lvl), lvl)
            construct_fractal((top_left[0] + 3 ** lvl + 3 ** lvl, top_left[1] + 3 ** lvl), (top_right[0] + 3 ** lvl + 3 ** lvl, top_right[1] - 3 ** lvl), (bottom_left[0], bottom_left[1] + 3 ** lvl), (bottom_right[0], bottom_right[1] - 3 ** lvl), lvl)
            construct_fractal((top_left[0] + 3 ** lvl + 3 ** lvl, top_left[1] + 3 ** lvl + 3 ** lvl), (top_right[0] + 3 ** lvl + 3 ** lvl, top_right[1]), (bottom_left[0], bottom_left[1] + 3 ** lvl + 3 ** lvl), bottom_right, lvl)

for _ in range(int(input())):
    n, b, t, l, r = int(input()), int(input()), int(input()), int(input()), int(input())
    b, t, l, r = b - 1, t - 1, l - 1, r - 1
    fractal = [["*" for i in range(3 ** n)] for j in range(3 ** n)]
    construct_fractal((0, 0), (0, 3 ** n - 1), (3 ** n - 1, 0), (3 ** n - 1, 3 ** n - 1), n)
    for i in range(t, b - 1, -1):
        print(" ".join(fractal[i][l:r + 1]))