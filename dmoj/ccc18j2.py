spots = int(input())
yesterday = []
today = []
occupied = 0

for char in input():
    yesterday.append(char)
for char in input():
    today.append(char)

for i in range(0,spots):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied+=1
    
print(occupied)