for i in range(int(input())):
    characters = list(input())
    output = []
    count = 0
    for j in range(len(characters)):
        if j == 0: # first character
            count = 1
        elif characters[j] != characters[j-1]: # when the string changes
            output.append(count)
            output.append(characters[j-1])
            count = 1
        else:
            count+=1
        if j == len(characters)-1: # last character
            output.append(count)
            output.append(characters[j])
    print(*output)