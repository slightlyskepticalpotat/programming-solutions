for _ in range(5):
    words = [word[::-1] for word in input().strip().split()][::-1]
    for i in range(len(words)):
        if all(char.isdigit() for char in words[i]):
            words[i] = words[i][::-1]
    print(" ".join(words))