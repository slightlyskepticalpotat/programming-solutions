import sys
input = sys.stdin.readline

casper = []
natalie = []
for i in range(int(input())):
    a, b = map(int, input().split())
    casper.append(a*b)
for i in range(int(input())):
    a, b = map(int, input().split())
    natalie.append(a*b)
if max(casper) > max(natalie):
    print("Casper")
elif max(natalie) > max(casper):
    print("Natalie")
else:
    print("Tie")