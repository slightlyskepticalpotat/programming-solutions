import sys
input = sys.stdin.readline

stuff = {}
for i in range(int(input())):
    letter, encoding = input().strip().split()
    stuff[encoding] = letter
ciphertext = list(input().strip())
plaintext = ""
queue = ""

for thing in ciphertext:
    queue += thing
    if queue in stuff.keys():
        plaintext += stuff[queue]
        queue = ""
print(plaintext)