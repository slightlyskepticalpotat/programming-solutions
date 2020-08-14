letters, bag = input().strip(), input().strip()
for char in set(letters):
    if letters.count(char) != bag.count(char):
        print(char)
        raise SystemExit