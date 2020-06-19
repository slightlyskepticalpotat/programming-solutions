sentence = [char for char in input().split()]
for i in range(len(sentence)):
    if sentence[i] != sentence[i].lower():
        sentence[i-1]+="."
print(*sentence)