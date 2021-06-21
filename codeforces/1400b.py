import sys

input = sys.stdin.readline

for _ in range(int(input())):
    p, f = map(int, input().split())
    cnt_s, cnt_w = map(int, input().split())
    s, w = map(int, input().split())
    ans = []
    if s > w: # make swords cheapest
        s, w, cnt_s, cnt_w = w, s, cnt_w, cnt_s
    for p_s in range(min(cnt_s, p // s) + 1):
        p_w = min(cnt_w, (p - s * (p_s)) // w)
        f_s = min(cnt_s - p_s, f // s)
        f_w = min(cnt_w - p_w, (f - f_s * s) // w)
        ans.append(p_s + p_w + f_s + f_w)
    print(max(ans))
