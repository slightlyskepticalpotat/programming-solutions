import sys
input = sys.stdin.readline

a, b = 0, 0

while True:
    instruction = input().strip()
    command = instruction[0:1]
    if command == "7": # exit
        break
    else:
        variable = instruction[2:3]
    
    if command == "1": # doing stuff
        if variable == "A":
            a = int(instruction[3:])
        else:
            b = int(instruction[3:])
    elif command == "2":
        if variable == "A":
            print(a)
        else:
            print(b)
    elif command == "3":
        second_variable = instruction[4:5].lower()
        variable = variable.lower()
        exec("{0} = {1} + {2}".format(variable, variable, second_variable))
    elif command == "4":
        second_variable = instruction[4:5].lower()
        variable = variable.lower()
        exec("{0} = {1} * {2}".format(variable, variable, second_variable))
    elif command == "5":
        second_variable = instruction[4:5].lower()
        variable = variable.lower()
        exec("{0} = {1} - {2}".format(variable, variable, second_variable))
    elif command == "6":
        second_variable = instruction[4:5].lower()
        variable = variable.lower()
        exec("{0} = {1} // {2}".format(variable, variable, second_variable))