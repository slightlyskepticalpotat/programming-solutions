for _ in range(int(input())):
    word = input().strip()
    if len(word) <= 10:
        print(word)
    else:
        print(word[0] + str(len(word) - 2) + word[-1])
