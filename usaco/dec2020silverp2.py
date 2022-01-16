def low(min_val, array, index):
    l = 0
    h = n - 1
    while l <= h:
        m = (l + h) // 2
        if array[m][index] >= min_val:
            h = m - 1
        else:
            l = m + 1
    return l

def high(max_val, array, index):
    l = 0
    h = n - 1
    while l <= h:
        m = (l + h) // 2
        if array[m][index] <= max_val:
            l = m + 1
        else:
            h = m - 1
    return h

def within(min_val, max_val, array, index):
    low_val = low(min_val, array, index)
    high_val = high(max_val, array, index)
    return frozenset(array[low_val:high_val + 1])

n, subsets = int(input()), set()
cows = [tuple([int(i) for i in input().split()] + [j]) for j in range(n)]
cows_x = sorted(cows, key = lambda x: x[0])
cows_y = sorted(cows, key = lambda x: x[1])

for cowa in cows_x:
    for cowb in cows_x:
        for cowc in cows_y:
            for cowd in cows_y:
                x_can = within(cowa[0], cowb[0], cows_x, 0)
                y_can = within(cowc[1], cowd[1], cows_y, 1)
                subsets.add(x_can.intersection(y_can))
print(len(subsets))
