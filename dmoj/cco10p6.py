plaintext, ciphertext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_", ""
for i in range(27):
    ciphertext += input().strip()
n, message = int(input()), input().strip()
cipher = str.maketrans(plaintext, ciphertext)

original_message, same = message, []
for i in range(2048): # find a cycle
    message = message.translate(cipher)
    if message == original_message:
        same.append(i)
    if len(same) == 2:
        n -= same[0]
        n = n % (same[1] - same[0]) - 1 # anything after is useless
        break
for i in range(n):
    message = message.translate(cipher)
print(message)