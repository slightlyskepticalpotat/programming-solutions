# take rightmost contiguous sequence of 1's
# take the leftmost 1
# switch it with the 0 to the left
# remaining 1's slide to the right

for i in range(5):
    n = int(input())
    rightmost = n & -n
    next_higher = n + int(rightmost)
    print(int(((next_higher ^ n) >> 2) / rightmost) | next_higher)