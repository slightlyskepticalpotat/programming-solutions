s = input().strip()

try:
    if -1 < s.rindex("o") < s.rindex("u") < s.rindex("r"):
        print("Y")
    else:
        print("N")
except:
    print("N")