upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
placeholder = int(input())
shift = int(input())
ciphertext = [char for char in input().strip()]
plaintext = []

for thing in ciphertext:
    if thing == " ":
        plaintext.append(" ")
    elif thing.isupper():
        plaintext.append(upper[(upper.index(thing)+shift)%26])
    elif thing.islower():
        plaintext.append(lower[(lower.index(thing)+shift)%26])
print("".join(plaintext))