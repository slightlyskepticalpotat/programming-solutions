import re
stuffs = re.findall('[A-Z][^A-Z]*', input())
nop = 0
for char in stuffs[:-1]:
    length = len(char)
    if length % 4 == 0:
        pass
    else:
        nop = nop + ((length//4)*4 + 4) - length
print(nop)