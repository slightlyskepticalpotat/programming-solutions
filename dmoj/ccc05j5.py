import sys
input = sys.stdin.readline

def is_monkey(x):
    while "ANA" in x or "BAS" in x:
        x = x.replace("ANA", "A")
        x = x.replace("BAS", "A")
    if x == "A":
        return True
    else:
        return False

while True:
    word = input().strip()
    if word == "X":
        break
    else:
        if is_monkey(word):
            print("YES")
        else:
            print("NO")