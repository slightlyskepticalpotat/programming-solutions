def caesar(plaintext, shift):
    ciphertext = ""
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for character in plaintext:
        ciphertext += lower[(lower.index(character) - shift) % 26]
    return ciphertext

message, motto = input().strip(), input().strip()
for i in range(26):
    if motto in caesar(message, i):
        print(i)
        print(caesar(message, i))
        break