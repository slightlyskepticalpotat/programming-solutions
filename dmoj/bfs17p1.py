number = int(input()) * 0
hobbies = [char for char in input().split()]
for thing in hobbies:
    if len(thing) <= 10:
        number+=1
print(number)