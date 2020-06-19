import sys
from collections import Counter

input = sys.stdin.readline

def mode(L):
    counter = Counter(L)
    max_count = max(counter.values())
    reet = [item for item, count in counter.items() if count == max_count]
    reet.sort()
    return reet

number = int(input())
data = list(map(int, input().split()))

ree = mode(data)
ree = [str(i) for i in ree]

print(' '.join(ree))