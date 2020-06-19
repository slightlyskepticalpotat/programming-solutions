blocks = []
for i in range(3):
    blocks.append(int(input()))
if blocks == sorted(blocks):
    print("Good job!")
else:
    print("Try again!")