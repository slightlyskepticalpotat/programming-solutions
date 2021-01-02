import sys

input = sys.stdin.readline

for _ in range(5):
    for i in range(3):
        raw_prop, flag = input().strip(), True
        distinct = list(set([char for char in raw_prop if char.isalpha()]))
        for i in range(2 ** len(distinct) + 1):
            proc_prop, mask = "", bin(i)[2:].zfill(len(distinct))
            for char in raw_prop:
                if char == "^":
                    proc_prop += " and "
                elif char == "v":
                    proc_prop += " or "
                elif char == "~":
                    proc_prop += " not "
                elif char in distinct:
                    proc_prop += (" " + mask[distinct.index(char)] + " ")
                else:
                    proc_prop += char
            if not eval(proc_prop):
                print("N", end = "")
                flag = False
                break
        if flag:
            print("Y", end = "")
    print("")