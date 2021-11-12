import sys

input = sys.stdin.readline

replace = [0, 1, 5, float("inf"), float("inf"), 2, float("inf"), float("inf"), 8, float("inf")]

def flip(x):
    ans = ""
    for char in x[::-1]:
        if char == ":":
            ans += char
        else:
            ans += str(replace[int(char)])
    return ans

def good(x, real_h, real_m):
    try:
        good_h, good_m = map(int, x.split(":"))
        return real_h - good_h >= 1 and real_m - good_m >= 1
    except:
        return False

for _ in range(int(input())):
    h, m = map(int, input().split())
    time_h, time_m = map(int, input().split(":"))
    while True:
        if time_m == m:
            time_h += 1
            time_m = 0
        if time_h == h:
            time_h = 0
        if good(flip(str(time_h).zfill(2) + ":" + str(time_m).zfill(2)), h, m):
            print(str(time_h).zfill(2) + ":" + str(time_m).zfill(2))
            break
        time_m += 1
