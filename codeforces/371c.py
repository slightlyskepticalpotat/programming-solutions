def price(x):
    return max(0, r_b * x - n_b) * p_b + max(0, r_s * x - n_s) * p_s + max(0, r_c * x - n_c) * p_c

recipe = input().strip()
r_b, r_s, r_c = recipe.count("B"), recipe.count("S"), recipe.count("C")
n_b, n_s, n_c = map(int, input().split())
p_b, p_s, p_c = map(int, input().split())
r = int(input())

low, mid, high, ans = 1, -1, 10 ** 16, 0
while low < high:
    mid = (high + low) // 2
    if price(mid) <= r < price(mid + 1):
        ans = mid
        break
    elif price(mid) <= r:
        low = mid + 1
    elif price(mid) > r:
        high = mid
print(ans)
