a, b, c = int(input()), int(input()), int(input())

if a + b > c and a + c > b and b + c > a:
    print("Huh? A triangle?")
else:
    print("Maybe I should go out to sea...")