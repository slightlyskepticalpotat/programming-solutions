text, numbers = [], []
for i in range(5):
    text.append([input().strip(), int(input())])

text.sort(key = lambda x: x[1])
for line in text:
    print(line[0])