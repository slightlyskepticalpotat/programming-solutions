import sys, math
input = sys.stdin.readline

def sublist(a, b):
    copy_a, copy_b = list(a), list(b)
    try:
        for char in a:
            copy_a.remove(char)
            copy_b.remove(char)
        return True
    except:
        return False
    
tiles, potential, worth = [], [0], {}
for i in range(int(input())):
    a, b, c = input().strip().split()
    for i in range(int(c)):
        tiles.append(a)
    worth[a] = int(b)

for i in range(int(input())):
    word = [char for char in input().strip()]
    score = 0
    if sublist(word, tiles):
        for char in word:
            score += (worth[char])
    potential.append(score)
print(max(potential))