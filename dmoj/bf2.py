ree = input()
length = int(input())

least = ree[0:length]

for i in range(len(ree) - length + 1):
    if ree[i:i+length] < least:
        least = ree[i:i+length]
print(least)