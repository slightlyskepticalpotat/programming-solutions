t, p = input()[::-1], input()
if p in t:
    print(len(t) - t.find(p))
else:
    print(-1)