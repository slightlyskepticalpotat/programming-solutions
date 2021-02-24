string = [char for char in input().strip()]
flag, current, last = False, 0, ""
for char in string:
    if char == last:
        current += 1
    else:
        current = 0
    last = char
    if current >= 6:
        flag = True
if flag:
    print("YES")
else:
    print("NO")
