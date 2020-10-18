for i in range(int(input())):
    ree = input() 
    if not "M" in ree and not "C" in ree:
        print("PASS")
    elif "M" in ree and "C" in ree:
        print("NEGATIVE MARKS")
    else:
        print("FAIL")