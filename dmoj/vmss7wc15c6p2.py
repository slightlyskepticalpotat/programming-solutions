for i in range(int(input())):
    words = []
    try:
        while True:
            text = [char for char in input().strip().split()]
            compressed = []
            if not text:
                print("") # placeholder empty line
                raise
            else:
                for word in text:
                    if word in words:
                        compressed.append(str(words.index(word) + 1))
                    else:
                        compressed.append(word)
                        words.append(word)
            print(" ".join(compressed))
    except:
        pass