pain = input().lower()
if pain.count("a") >= (pain.count("e") + pain.count("i") + pain.count("o") + pain.count("u")):
    print("Advance to next round")
else:
    print("Does not advance to next round")