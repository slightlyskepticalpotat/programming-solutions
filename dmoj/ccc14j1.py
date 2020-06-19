angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

angle_sum = angle1 + angle2 + angle3

if angle_sum != 180:
    print('Error')
    
else:
    if angle1 == 60 and angle2 == 60 and angle3 == 60:
        print('Equilateral')
    else:
        if angle1 == angle2 or angle2 == angle3 or angle3 == angle1:
            print('Isosceles')
        else:
            print('Scalene')