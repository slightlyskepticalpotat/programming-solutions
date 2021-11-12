def works(v):
    shared = v // (x * y)
    cnt_1loc, cnt_2loc = v // x, v // y
    split = v - cnt_1loc - cnt_2loc + shared
    cnt_1loc, cnt_2loc = cnt_1loc - shared, cnt_2loc - shared
    return (max(cnt1 - cnt_2loc, 0) + max(cnt2 - cnt_1loc, 0)) <= split

cnt1, cnt2, x, y = map(int, input().split())
low, mid, high = 0, -1, 10 ** 18
while high - low > 1:
    mid = (high + low) // 2
    if works(mid):
        high = mid
    else:
        low = mid
print(high)
