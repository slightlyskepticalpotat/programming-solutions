import sys
input = sys.stdin.readline

low, high = 1, 2000000000
while True:
    mid = (low + high) // 2
    print(mid)
    result = input().strip()
    if result == "SINKS":
        low = mid + 1
    elif result == "FLOATS":
        high = mid - 1
    elif result == "OK":
        break