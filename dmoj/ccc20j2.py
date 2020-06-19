import sys, copy
input = sys.stdin.readline

p = int(input()) #goal
n = int(input()) #start
r = int(input()) #infectivity

day = 0
infected = n
infected_day = n

while True:
    infected = infected*r 
    infected_day += infected

    day+=1
    
    if infected_day > p:
        print(day)
        break
    else:
        pass