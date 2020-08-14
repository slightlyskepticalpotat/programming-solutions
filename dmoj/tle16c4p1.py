number, total, presents = 0, 0, []
for i in range(int(input())):
    presents.append(int(input()))
presents.sort()

for thing in presents:
    if thing >= total:
        number+=1
        total += thing
print(number)