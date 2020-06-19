import sys
from collections import Counter 

input = sys.stdin.readline


str1 = input().strip()
str2 = input().strip()

str1 = list([char for char in str1])
str2 = list([char for char in str2])


if len(list((Counter(str1) - Counter(str2)).elements())) == 1:
    print('LARRY IS SAVED!')
else:
    print('LARRY IS DEAD!')