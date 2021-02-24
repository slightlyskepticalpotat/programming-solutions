k, text = int(input()), input().strip()
freqs = [text.count(char) for char in set(text)]
if all(freq % k == 0 for freq in freqs):
    print(k * "".join([char * (text.count(char) // k) for char in set(text)]))
else:
    print(-1)
