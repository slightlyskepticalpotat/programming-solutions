ree = "123456789abcdefghijklmnopqrstuvwxyz0"

for i in range(int(input())):
    a, operator, b, equals, c = input().strip().split()
    result = ["invalid"]
    
    if eval(str(len(a)) + operator + str(len(b))) == len(c) and str(a).replace("1", "") == "": # python no support for base 1, for some reason
        result.append(str(1))
    for i in range(2, 37):
        try:
            if eval(str(int(a, i)) + operator + str(int(b, i))) == int(c, i):
                result.append(ree[i-1:i])
        except:
            pass
    if len(result) > 1:
        print("".join(result[1:]))
    else:
        print(result[0])