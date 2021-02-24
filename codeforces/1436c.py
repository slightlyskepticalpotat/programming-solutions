import math

n, x, p = map(int, input().split())
low, high, less_count, more_count = 0, n, 0, 0
while low < high:
    mid = (low + high) // 2
    if mid > p:
        more_count += 1
        high = mid
    else:
        less_count += int(p != mid)
        low = mid + 1
        
left, avail_less, avail_more = n - less_count - more_count - 1, x - 1, n - x
less_choices, more_choices = (math.comb(avail_less, less_count) * math.factorial(less_count)) % (10 ** 9 + 7), (math.comb(avail_more, more_count) * math.factorial(more_count)) % (10 ** 9 + 7)
print((less_choices * more_choices * math.factorial(left)) % (10 ** 9 + 7))
