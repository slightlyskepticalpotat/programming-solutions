import sys
input = sys.stdin.readline

small = int(input())*1
medium = int(input())*2
big = int(input())*3

happy = small + medium + big

if happy >= 10:
    print('happy')
else:
    print('sad')