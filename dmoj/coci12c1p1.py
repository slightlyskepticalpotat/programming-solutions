remove = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]
text = input().strip()
for thing in remove:
    text = text.replace(thing, "")
print(text)