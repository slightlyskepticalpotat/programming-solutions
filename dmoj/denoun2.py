import sys
input = sys.stdin.readline

punctuation = list('''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~''')
for i in range(int(input())):
    text = [char for char in input().split()]
    for thing in text:
        for symbol in punctuation:
            thing = thing.replace(symbol, "")
        if thing != thing.lower():
            print(thing)