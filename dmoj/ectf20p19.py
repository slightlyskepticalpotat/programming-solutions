location = input().strip()[2:]
location = [chr(int(location[i:i+2], 16)) for i in range(0, len(location), 2)]
print("e" * 119 + "".join(reversed(location)))