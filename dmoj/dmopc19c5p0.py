import sys
input = sys.stdin.readline
people, cutoff = input().split()
people, cutoff = int(people), int(cutoff)

for i in range(0, people):
    person, score = input().split()
    score = int(score)
    if score > cutoff:
        print(person, 'will advance')
    else:
        print(person, 'will not advance')