# https://regex101.com/
import re

for i in range(int(input())):
    text = [char for char in input().strip().split()]
    for i in range(len(text)):
        text[i] = re.sub("(?<![^\W_])[a-zA-Z0-9]{4}(?![^\W_])", "****", text[i])
    print(" ".join(text))