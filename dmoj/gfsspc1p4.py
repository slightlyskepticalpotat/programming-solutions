import sys

dna_length = int(sys.stdin.readline())
dna = list(sys.stdin.readline().strip())
fibs = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
flag = 0

for i in range(0, len(dna)):
    if dna[i] == 'A':
        if i+1 in fibs:
            pass
        else:
            print('Bruno, GO TO SLEEP')
            flag = 1
            break
    else:
        if i+1 in fibs:
            print('Bruno, GO TO SLEEP')
            flag = 1
            break
if flag == 0:
    print("That's quite the observation!")
else:
    pass