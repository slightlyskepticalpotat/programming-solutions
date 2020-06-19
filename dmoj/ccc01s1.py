remaining = input().strip()
clubs, remaining = remaining.split("D")
clubs = [char for char in clubs]
diamonds, remaining = remaining.split("H")
diamonds = [char for char in diamonds]
hearts, spades = remaining.split("S")
hearts = [char for char in hearts]
spades = [char for char in spades]

for thing in clubs:
    if thing == "C":
        clubs.remove(thing)
        
def points(thing):
    points = 0
    if len(thing) == 0:
        points+=3
    elif len(thing) == 1:
        points+=2
    elif len(thing) == 2:
        points+=1
    for char in thing:
        if char == "A":
            points+=4
        elif char == "K":
            points+=3
        elif char == "Q":
            points+=2
        elif char == "J":
            points+=1
    return points

print("Cards Dealt  Points")
print("Clubs", end=" ")
print(*clubs, end= "  ")
print(points(clubs))
print("Diamonds", end=" ")
print(*diamonds, end= "  ")
print(points(diamonds))
print("Hearts", end=" ")
print(*hearts, end= "  ")
print(points(hearts))
print("Spades", end=" ")
print(*spades, end= "  ")
print(points(spades))
print("", end="  ")
print("Total", end="  ")
print(points(clubs)+points(diamonds)+points(hearts)+points(spades))