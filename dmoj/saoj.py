ree = int(input())
answer = 0
for i in range(1, ree+1):
    answer+=i**6
print(answer%1000000000)