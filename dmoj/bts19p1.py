import sys
from itertools import chain

words = []
word = 'k'
closest = 'k'
distance = 1000
current = 0

k = sys.stdin.readline()
words.append(sys.stdin.readline().strip().split(' '))

word = sys.stdin.readline().strip()

words = list(chain.from_iterable(words))

for i in words:
    if len(i) > len(word):
        pass
    else:
        current = int(len(word)-len(i))
        if current <= distance:
            closest = i
            distance = current
        else:
            pass
            
print(closest)