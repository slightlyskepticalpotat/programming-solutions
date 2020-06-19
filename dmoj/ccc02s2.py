import math
from fractions import Fraction
num = int(input())
de_num = int(input())

whole = int(math.floor(num/de_num))

answer2 = num % de_num

answer2 = str(Fraction(answer2, de_num))


if eval(answer2) == 0:
    print(whole)
elif int(whole == 0):
    print(answer2)
else:
    print(whole, answer2)