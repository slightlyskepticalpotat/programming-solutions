import sys
input = sys.stdin.readline

samples = {int(input()) for i in range(int(input()))} # has to be unique, m=100000 but only 100 percentages

for i in range(1, 101):
    percents = {int(100 * j / i + 0.5) for j in range(i + 1)} # every probability
    if samples.issubset(percents):
        print(i)
        break