import sys

input = sys.stdin.readline

s, k = input().strip(), int(input())
characters, answer = {}, 0

for i in range(k):
    characters[s[i]] = characters.get(s[i], 0) + 1 # 0 is default value
if len(characters.keys()) == 1:
    answer += 1

for i in range(k, len(s)): # sliding window
    characters[s[i]] = characters.get(s[i], 0) + 1 # 0 is default value
    characters[s[i - k]] -= 1
    if characters[s[i - k]] == 0:
        del characters[s[i - k]]
    if len(characters.keys()) == 1:
        answer += 1
print(answer)