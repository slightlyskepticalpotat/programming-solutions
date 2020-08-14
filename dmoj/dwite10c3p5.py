import re

for i in range(5):
    dictionary = []
    for _ in range(int(input())): # build dictionary
        dictionary.append(input().strip())
    for _ in range(5): # build regex
        answer = []
        query = [char for char in input().strip()]
        for j in range(len(query)):
            if query[j].isalpha():
                query[j] = query[j] + "{1}"
            elif query[j] == "?":
                query[j] = ".{1}"
            elif query[j] == "*":
                query[j] = ".{0,}"
        query = "".join(query) + "$"
        
        for thing in dictionary:
            try:
                answer += re.findall(query, thing)
            except:
                pass
        if answer:
            print(", ".join([char for char in answer if char != ""]))
        else:
            print("NO MATCH")