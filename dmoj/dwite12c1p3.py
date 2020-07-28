for i in range(5):
    costumes, switch = [], []
    for i in range(int(input())):
        person, costume = input().split()
        if costume in costumes:
            switch.append(person)
        else:
            costumes.append(costume)
    if len(switch) > 0:
        print(*switch)
    else:
        print("SPOOKY")