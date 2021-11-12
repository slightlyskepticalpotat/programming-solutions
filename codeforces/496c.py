n, m = map(int, input().split())
words, needed, final = [input().strip() for _ in range(n)], 0, ["" for _ in range(n)]
for i in range(m):
    extended = [final[j] + words[j][i] for j in range(n)]
    if extended == list(sorted(extended)):
        final = extended
    needed += int(not extended == list(sorted(extended)))
print(needed)
