actions = input().strip()
for i in range(len(actions)):
    if actions[i] == "r":
        print(i + 1)
for i in range(len(actions) - 1, -1, -1):
    if actions[i] == "l":
        print(i + 1)
