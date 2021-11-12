e = [char for char in input().strip()][::-1]
flag = False
while e:
    if e.pop() == "h":
        while e:
            if e.pop() == "e":
                while e:
                    if e.pop() == "l":
                        while e:
                            if e.pop() == "l":
                                while e:
                                    if e.pop() == "o":
                                        flag = True
                                        break
                                    else:
                                        pass
                                break
                            else:
                                pass
                        break
                    else:
                        pass
                break
            else:
                pass
        break
    else:
        pass
if flag:
    print("YES")
else:
    print("NO")
