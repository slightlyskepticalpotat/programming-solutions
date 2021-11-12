string = input().strip()
count = str(string.count("4") + string.count("7"))
if all(char in ["4", "7"] for char in count):
    print("YES")
else:
    print("NO")
