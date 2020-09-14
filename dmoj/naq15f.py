alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
for i in range(int(input())):
    sentence = set([char for char in input().strip().lower() if char in alphabet])
    if len(sentence) == 26:
        print("pangram")
    else:
        print(f'''missing {"".join(sorted(alphabet.difference(sentence)))}''')