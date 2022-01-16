s, freq, ans = input().strip(), {i: 0 for i in "abcdefghijklmnopqrstuvwxyz"}, 1
for char in s:
    freq[char] += 1
freq = {key: freq[key] + 1 for key in freq}
for key in freq:
    ans = (ans * freq[key]) % (10 ** 9 + 7)
print(ans)