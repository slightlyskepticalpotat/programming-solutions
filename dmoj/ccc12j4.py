k = int(input())
decode = [char for char in input().strip()]
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0, len(decode)):
    shift = (3*(i+1)+k) % 26
    decode[i] = chars[(chars.index(decode[i])-shift)%26]
print("".join(decode))