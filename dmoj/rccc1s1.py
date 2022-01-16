import itertools

n, c, v = map(int, input().split())
word, flag = input().strip(), True
vowels = [char in "aeiouy" for char in word]
consonants = [char in "bcdfghjklmnpqrstvwxyz" for char in word]
vowels = [[x, len(list(y))] for x, y in itertools.groupby(vowels)]
consonants = [[x, len(list(y))] for x, y in itertools.groupby(consonants)]
for section in vowels:
    if section[0] and section[1] > v:
        flag = False
for section in consonants:
    if section[0] and section[1] > c:
        flag = False
if flag:
    print("YES")
else:
    print("NO")