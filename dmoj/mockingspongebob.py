import sys
input = sys.stdin.readline

for i in range(int(input())):
    counter = 0
    text = [char for char in input().strip()]
    
    for i in range(len(text)):
        if text[i].isalpha():
            if counter % 2 == 0:
                text[i] = text[i].lower()
            else:
                text[i] = text[i].upper()
            counter+=1
    
    print(''.join(text))