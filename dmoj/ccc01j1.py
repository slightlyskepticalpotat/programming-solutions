import math

size = int(input())
stars = 2
spaces = size*2-stars

for i in range(0,int(math.ceil(size/2))):
    print('*'*int((stars/2)) + spaces*' ' + '*'*int((stars/2)))
    stars+=4
    spaces = size*2-stars

stars = size*2-4
spaces = size*2-stars

for i in range(0,int(math.floor(size/2))):
    print('*'*int((stars/2)) + spaces*' ' + '*'*int((stars/2)))
    stars-=4
    spaces = size*2-stars