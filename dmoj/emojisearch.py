import re

text = re.findall(":{1}.*?:{1}", input().strip())
for thing in text:
    print(thing[1:-1])