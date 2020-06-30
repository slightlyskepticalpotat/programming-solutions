straw = ""
for i in range(7):
    straw+=input().strip()
while "JJ" in straw:
    straw = straw.replace("JJ", "J")
print(straw.count("J"))