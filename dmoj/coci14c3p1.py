one, two, three, four, five, six, seven, eight = 0, 0, 0, 0, 0, 0, 0, 0
for thing in list(input().strip()):
    if thing in "1QAZ":
        one += 1
    elif thing in "2WSX":
        two += 1
    elif thing in "3EDC":
        three += 1
    elif thing in "45RTFGVB":
        four += 1
    elif thing in "67YUHJNM":
        five += 1
    elif thing in "8IK,":
        six += 1
    elif thing in "9OL.":
        seven += 1
    elif thing in "0-=P[];'/":
        eight += 1
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)