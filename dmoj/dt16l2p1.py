liczby = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
całkowity = 0
while True:
    numer = input().strip()
    if numer == "No more numbers.":
        break
    else:
        całkowity += liczby[numer]
print(całkowity)