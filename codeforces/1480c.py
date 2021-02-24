def get(x):
    if values[x] == -1:
        print(f"? {x + 1}")
        values[x] = int(input())
    return values[x]

n = int(input())
low, mid, high = 0, -1, n - 1
values = [-1 for _ in range(n)]
while True:
    mid = (low + high) // 2
    if n == 1:
        mid = 0
        break
    elif mid == 0 and get(mid) < get(mid + 1) or mid == n - 1 and get(mid) < get(mid - 1):
        break
    elif n == 2:
        if get(0) < get(1):
            mid = 0
            break
        else:
            mid = 1
            break
    elif get(mid - 1) > get(mid) < get(mid + 1):
        break
    elif get(mid) > get(mid - 1):
        high = mid
    else:
        low = mid + 1
print(f"! {mid + 1}")
