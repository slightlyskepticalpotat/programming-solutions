def bar():
    print(" * * *\n", end = "")
def leftbar():
    print("*\n", end = "")
    print("*\n", end = "")
    print("*\n", end = "")
def rightbar():
    print("      *\n", end = "")
    print("      *\n", end = "")
    print("      *\n", end = "")
def bothbar():
    print("*     *\n", end = "")
    print("*     *\n", end = "")
    print("*     *\n", end = "")
def space():
    print("\n", end = "")

number = int(input())
if number == 0:
    bar()
    bothbar()
    space()
    bothbar()
    bar()
elif number == 1:
    space()
    rightbar()
    space()
    rightbar()
    space()
elif number == 2:
    bar()
    rightbar()
    bar()
    leftbar()
    bar()
elif number == 3:
    bar()
    rightbar()
    bar()
    rightbar()
    bar()
elif number == 4:
    space()
    bothbar()
    bar()
    rightbar()
    space()
elif number == 5:
    bar()
    leftbar()
    bar()
    rightbar()
    bar()
elif number == 6:
    bar()
    leftbar()
    bar()
    bothbar()
    bar()
elif number == 7:
    bar()
    rightbar()
    space()
    rightbar()
    space()
elif number == 8:
    bar()
    bothbar()
    bar()
    bothbar()
    bar()
elif number == 9:
    bar()
    bothbar()
    bar()
    rightbar()
    bar()