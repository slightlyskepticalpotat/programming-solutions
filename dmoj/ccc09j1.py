digit1 = int(input())
digit2 = int(input())
digit3 = int(input())

isbn_sum = 91

isbn_sum = isbn_sum + 1*digit1 + 3*digit2 + 1*digit3

print('The 1-3-sum is %s' % isbn_sum)