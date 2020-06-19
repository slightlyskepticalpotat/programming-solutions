ree = [char for char in input().strip()]
u, l = 0, 0

for thing in ree:
    if thing.isupper():
        u += 1
    elif thing.islower():
        l+=1
        
if u > l:
    print("".join(ree).upper())
elif l > u:
    print("".join(ree).lower())
else:
    print("".join(ree))