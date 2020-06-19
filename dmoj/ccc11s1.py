cases = int(input())
text = []

for i in range(0,cases):
    text.append(input().lower())
text = ' '.join(text)

s = text.count('s')
t = text.count('t')

if t > s:
    print('English')
else:
    print('French')