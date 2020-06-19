import sys
palin = []

word = sys.stdin.readline()

def substrings(word):
    substring = []
    for i in range(len(word)):
        for j in range(i, len(word)):
            substring.append(word[i:j+1])
    return substring
    
for elem in substrings(word):
    if elem == elem[::-1]:
        palin.append(elem)
    else:
        pass
    
print(len(max(palin,key=len)))