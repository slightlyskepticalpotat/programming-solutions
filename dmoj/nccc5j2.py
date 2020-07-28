import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
numbers = [int(i) for i in input().split()]
counter = Counter(numbers)
print(min(thing for thing, count in counter.items() if count == counter.most_common(1)[0][1]))