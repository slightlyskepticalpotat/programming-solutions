# please dm me on discord if you see this, along with a short explanation of why you're stalking my submissions

import sys
input = sys.stdin.readline

cases = int(input())

for i in range(0, cases):
    text = input()
    words = text.split()
    for i in range(0,len(words)):
        if len(words[i]) == 4:
            words[i] = '****'
    text = ' '.join(words)
    print(text)