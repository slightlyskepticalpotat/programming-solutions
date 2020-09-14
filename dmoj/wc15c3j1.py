a_b, d_b = map(int, input().split())
a_s, d_s = map(int, input().split())

if a_b > d_s and d_b > a_s:
    print("Batman")
elif a_s > d_b and d_s > a_b:
    print("Superman")
else:
    print("Inconclusive")