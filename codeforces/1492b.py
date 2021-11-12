import sys

input = sys.stdin.readline

for _ in range(int(input())): # kth original element = maximum element
    n, cards, nums = int(input()), [int(i) for i in input().split()], {}
    ans, last = [], n
    for i in range(n):
        nums[cards[i]] = i
    for i in range(n, 0, -1):
        if nums[i] <= last:
            ans += cards[nums[i]:last]
            last = nums[i]
    print(*ans)
