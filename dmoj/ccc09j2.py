trout = int(input())
pike = int(input())
pickerel = int(input())
total = int(input())
ways = 0
for i in range(total//trout+1):
    for j in range(total//pike+1):
        for k in range(total//pickerel+1):
            if i+j+k != 0 and i*trout + j*pike + k*pickerel <= total:
                print("{trout} Brown Trout, {pike} Northern Pike, {pickerel} Yellow Pickerel".format(trout=i, pike=j, pickerel=k))
                ways +=1
print("Number of ways to catch fish: {ways}".format(ways=ways))