import sys
input = sys.stdin.readline
plaintext = [char for char in input().strip()]
ciphertext = [char for char in input().strip()]
encoded = [char for char in input().strip()]
decoded = []
cipher = dict(zip(ciphertext, plaintext))

for char in encoded:
    if char in cipher.keys():
        decoded.append(cipher[char])
    else:
        decoded.append(".")
print("".join(decoded))