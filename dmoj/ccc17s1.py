from itertools import chain

games = int(input())
sw = []
se = []
days = []
swtotal = 0
setotal = 0
day = 1

sw.append(input().split())
se.append(input().split())
    
sw = list(chain.from_iterable(sw))
se = list(chain.from_iterable(se))


for i in range(0,games):
    swtotal = swtotal + int(sw[i])
    setotal = setotal + int(se[i])
    if swtotal == setotal:
        days.append(int(day))
    else:
        pass
    day+=1
if days == []:
    print(0)
else:
    print(max(days))