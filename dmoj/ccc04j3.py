adjectives = int(input())
nouns = int(input())

adjective_list = []
noun_list = []

for i in range(0, adjectives):
    adjective_list.append(input())
    
for i in range(0, nouns):
    noun_list.append(input())

for i in adjective_list:
    for j in noun_list:
        print(i,'as',j)