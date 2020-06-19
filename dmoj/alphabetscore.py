def main():
    r = input()
    l = "abcdefghijklmnopqrstuvwxyz"
    s = 0
    for i in range(26):
        s+=(r.count(l[i])*(i+1))
    print(s)
main()