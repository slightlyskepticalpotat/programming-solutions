import sys
input = sys.stdin.readline

cases = int(input())
for i in range(cases):
    x_pos, y_pos = 0, 0
    direction = 0
    while True:
        instruction = int(input())
        if instruction == 0:
            break
        elif instruction == 1:
            distance = int(input())
            if direction == 0:
                y_pos += distance
            elif direction == 90:
                x_pos += distance
            elif direction == 180:
                y_pos -= distance
            elif direction == 270:
                x_pos -= distance
        elif instruction == 2: # right
            direction = (direction + 90) % 360
        elif instruction == 3: # left
            direction = (direction + 270) % 360
            
    print("Distance is {distance}".format(distance=abs(x_pos)+abs(y_pos)))
    if x_pos == 0 and y_pos == 0:
        pass
    elif x_pos > 0 and y_pos == 0:
        if direction == 0:
            print(3)
        elif direction == 90:
            print(3)
            print(3)
        elif direction == 180:
            print(2)
        elif direction == 270:
            pass
        print(1)
        print(abs(x_pos))
    elif x_pos < 0 and y_pos == 0:
        if direction == 0:
            print(2)
        elif direction == 90:
            pass
        elif direction == 180:
            print(3)
        elif direction == 270:
            print(3)
            print(3)
        print(1)
        print(abs(x_pos))
    elif x_pos == 0 and y_pos > 0:
        if direction == 0:
            print(3)
            print(3)
        elif direction == 90:
            print(2)
        elif direction == 180:
            pass
        elif direction == 270:
            print(3)
        print(1)
        print(abs(y_pos))
    elif x_pos == 0 and y_pos < 0:
        if direction == 0:
            pass
        elif direction == 90:
            print(3)
        elif direction == 180:
            print(3)
            print(3)
        elif direction == 270:
            print(2)
        print(1)
        print(abs(y_pos))
    elif x_pos > 0 and y_pos > 0:
        if direction == 0:
            print(3)
            print(1)
            print(abs(x_pos))
            print(3)
            print(1)
            print(abs(y_pos))
        elif direction == 90:
            print(2)
            print(1)
            print(abs(y_pos))
            print(2)
            print(1)
            print(abs(x_pos))
        elif direction == 180:
            print(1)
            print(abs(y_pos))
            print(2)
            print(1)
            print(abs(x_pos))
        elif direction == 270:
            print(1)
            print(abs(x_pos))
            print(3)
            print(1)
            print(abs(y_pos))
    elif x_pos > 0 and y_pos < 0:
        if direction == 0:
            print(1)
            print(abs(y_pos))
            print(3)
            print(1)
            print(abs(x_pos))
        elif direction == 90:
            print(3)
            print(1)
            print(abs(y_pos))
            print(3)
            print(1)
            print(abs(x_pos))
        elif direction == 180:
            print(2)
            print(1)
            print(abs(x_pos))
            print(2)
            print(1)
            print(abs(y_pos))
        elif direction == 270:
            print(1)
            print(abs(x_pos))
            print(2)
            print(1)
            print(abs(y_pos))
    elif x_pos < 0 and y_pos > 0:
        if direction == 0:
            print(2)
            print(1)
            print(abs(x_pos))
            print(2)
            print(1)
            print(abs(y_pos))
        elif direction == 90:
            print(1)
            print(abs(x_pos))
            print(2)
            print(1)
            print(abs(y_pos))
        elif direction == 180:
            print(1)
            print(abs(y_pos))
            print(3)
            print(1)
            print(abs(x_pos))
        elif direction == 270:
            print(3)
            print(1)
            print(abs(y_pos))
            print(3)
            print(1)
            print(abs(x_pos))
    elif x_pos < 0 and y_pos < 0:
        if direction == 0:
            print(1)
            print(abs(y_pos))
            print(2)
            print(1)
            print(abs(x_pos))
        elif direction == 90:
            print(1)
            print(abs(x_pos))
            print(3)
            print(1)
            print(abs(y_pos))
        elif direction == 180:
            print(3)
            print(1)
            print(abs(x_pos))
            print(3)
            print(1)
            print(abs(y_pos))
        elif direction == 270:
            print(2)
            print(1)
            print(abs(y_pos))
            print(2)
            print(1)
            print(abs(x_pos))
    if i != cases-1:
        print("")