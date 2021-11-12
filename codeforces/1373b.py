import sys 

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    if min(s.count("0"), s.count("1")) % 2:
        print("DA")
    else:
        print("NET")