import sys
input = sys.stdin.readline

array = [0] * 1000001 # array[i] is the max wow factor for time i
for i in range(int(input())):
    time, wow = map(int, input().split())
    if wow > array[time]: # same time has 2 different wow values
        array[time] = wow # set the wow value for that time
for j in range(1000000): # compare arrays from left to right
    array[j+1] = max(array[j], array[j+1]) # if better wow, change it

for i in range(int(input())):
    print(array[int(input())])