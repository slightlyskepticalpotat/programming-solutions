def questions(x):
    return x//2 - x//7

minutes = int(input())
low, high = 0, 10**30

while low <= (high):
    mid = (low+high)//2

    if questions(mid) < minutes:
        low = mid + 1
    elif questions(mid) > minutes:
        high = mid - 1
    else:
        low = mid
        break

for i in range(low, low + 6):
    if questions(i) <= minutes:
        low = i

print(low)