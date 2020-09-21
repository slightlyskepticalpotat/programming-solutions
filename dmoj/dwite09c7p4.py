import re

for i in range(5):
    expression = input().strip()
    print(eval(re.sub(r'([\d]+|\(.*\))(?:\^)([\d]+|\(.*\))', r'int(str((abs(\1))) + str(abs((\2))))', expression))) # black magic trickery to replace all digits or bracket-surrounded groups