var1 = int(input())
var2 = int(input())
ree = [var1, var2]

length = 2


while True:
    ree.append(abs(ree[-1]-ree[-2]))
    if ree[-1] > ree[-2]:
        length+=1
        break
    else:
        length+=1
        
print(length)