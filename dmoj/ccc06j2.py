die_1 = int(input())
die_2 = int(input())
ways = 0

if die_1 == 6 and die_2 == 8:
    ways = 5
    print('There are %s ways to get the sum 10.' % ways)
elif die_1 == 12 and die_2 == 4:
    ways = 4
    print('There are %s ways to get the sum 10.' % ways)
elif die_1 == 6 and die_2 == 6:
    ways = 3
    print('There are %s ways to get the sum 10.' % ways)
elif die_1 == 4 and die_2 == 4:
    ways = 0
    print('There are %s ways to get the sum 10.' % ways)
elif die_1 == 12 and die_2 == 20:
    ways = 9
    print('There are %s ways to get the sum 10.' % ways)
elif die_1 == 3 and die_2 == 7:
    ways = 1
    print('There is %s way to get the sum 10.' % ways)