import sys, datetime
input = sys.stdin.readline

def validate(x):
    try:
        datetime.datetime.strptime(x, "%Y-%m-%d") # regex is overrated
        return True
    except:
        return False
    
for i in range(int(input())):
    text = input().strip()
    for j in range(len(text) - 9):
        if validate(text[j:j+10]):
            print(text[j:j+10])