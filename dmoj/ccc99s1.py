a, b, cards = 0, 0, []
for i in range(52):
    cards.append(input().strip())

def highcard(x):
    for thing in x:
        if thing in ["ace", "king", "queen", "jack"]:
            return True
    return False

for i in range(52):
    current = cards[i]
    if i % 2 == 0: # player a
        if current == "ace":
            if (51 - i) >= 4:
                if highcard(cards[i+1:i+3]) == False:
                    a += 4
                    print("Player A scores 4 point(s).")
        elif current == "king":
            if (51 - i) >= 3:
                if highcard(cards[i+1:i+4]) == False:
                    a += 3
                    print("Player A scores 3 point(s).")
        elif current == "queen":
            if (51 - i) >= 2:
                if highcard(cards[i+1:i+3]) == False:
                    a += 2
                    print("Player A scores 2 point(s).")
        elif current == "jack":
            if (51 - i) >= 1:
                if highcard(cards[i+1:i+2]) == False:
                    a += 1
                    print("Player A scores 1 point(s).")
    else: # player b
        if current == "ace":
            if (51 - i) >= 4:
                if highcard(cards[i+1:i+5]) == False:
                    b += 4
                    print("Player B scores 4 point(s).")
        elif current == "king":
            if (51 - i) >= 3:
                if highcard(cards[i+1:i+4]) == False:
                    b += 3
                    print("Player B scores 3 point(s).")
        elif current == "queen":
            if (51 - i) >= 2:
                if highcard(cards[i+1:i+3]) == False:
                    b += 2
                    print("Player B scores 2 point(s).")
        elif current == "jack":
            if (51 - i) >= 1:
                if highcard(cards[i+1:i+2]) == False:
                    b += 1
                    print("Player B scores 1 point(s).")
print(f"Player A: {a} point(s).")
print(f"Player B: {b} point(s).")