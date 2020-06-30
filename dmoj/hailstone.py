n = int(input())
operations = 0
while n != 1:
    if n % 2 == 1:
        n = n*3 +1
    else:
        n = n/2
    operations+=1
print(operations)