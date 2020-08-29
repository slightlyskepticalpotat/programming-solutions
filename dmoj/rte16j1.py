import sys
input = sys.stdin.readline

text = input().replace(" ", "")

c, m = 0, 0 # consecutive, maximum
for thing in text:
	if thing == "L":
		c += 1
	else:
		m = max(m, c)
		c = 0
print(text.count("L"), m)