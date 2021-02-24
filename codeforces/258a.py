string, flag = input().strip(), True
for i in range(len(string)):
    if string[i] == "0":
        print(string[:i] + string[i + 1:])
        flag = False
        break
if flag:
    print(string[:-1])
