string = input().strip()
convert = {"0": "O", "1": "l", "3": "E", "4": "A", "5": "S", "6": "G", "8": "B", "9": "g"}
for char in string:
    if char in convert.keys():
        print(convert[char], end = "")
    else:
        print(char, end = "")
print("")