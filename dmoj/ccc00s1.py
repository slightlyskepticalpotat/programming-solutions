quarters = int(input())
first_count = int(input())
second_count = int(input())
third_count = int(input())
which_played = 1

while quarters > 0:
    if which_played % 3 == 1:
        quarters-=1
        first_count+=1
        if first_count % 35 == 0:
            quarters+=30
    if which_played % 3 == 2:
        quarters-=1
        second_count+=1
        if second_count % 100 == 0:
            quarters+=60
    if which_played % 3 == 0:
        quarters-=1
        third_count+=1
        if third_count % 10 == 0:
            quarters+=9
    which_played+=1
    if quarters == 0:
        print('Martha plays {} times before going broke.'.format(which_played-1))