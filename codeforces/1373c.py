import sys 

input = sys.stdin.readline

for _ in range(int(input())):
    s, level, res, low = input().strip(), 0, 0, 0
    for i in range(len(s)): # psa-lite
        level += (1 if s[i] == "+" else -1)
        if level < low: # ends iteration
            low = level 
            res += i + 1
    print(res + len(s)) # first pass