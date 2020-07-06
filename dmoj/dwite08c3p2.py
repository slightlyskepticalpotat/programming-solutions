for i in range(5):
    count = 0
    sentence = [char for char in input().strip().replace("'", "zzzz").split()]
    sentence = ["".join(filter(str.isalnum, char)) for char in sentence]
    for word in sentence:
        if "zzzz" in word:
            count+=0
        elif len(word) >= 4:
            count+=1
    print(count)