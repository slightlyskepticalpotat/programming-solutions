def bar():
    print(" * * *")
def leftbar():
    print("*")
    print("*")
    print("*")
def rightbar():
    print("      *")
    print("      *")
    print("      *")
def bothbar():
    print("*     *")
    print("*     *")
    print("*     *")
def space():
    print("")
    
number = int(input())
if number == 0:
    bar()
    bothbar()
    space()
    bothbar()
    bar()
elif number == 1:
    rightbar()
    space()
    rightbar()
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
    bothbar()
    bar()
    rightbar()
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
    rightbar()
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