max_minutes = int(input())
max_chores = int(input())

chores = []
chores_time = 0
number_of_chores = 0
chores_count = 0

for i in range(0,max_chores):
    chore_time = int(input())
    chores.append(chore_time)
    
chores.sort()

while True:
    chores_time = chores_time + chores[chores_count]
    number_of_chores+=1

    if chores_time > max_minutes:
        print(number_of_chores - 1)
        break
    elif chores_time == max_minutes:
        print(number_of_chores)
        break
    else:
        chores_count+=1