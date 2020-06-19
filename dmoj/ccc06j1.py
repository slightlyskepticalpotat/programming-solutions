burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

calories = 0

if burger == 1:
    calories += 461
elif burger == 2:
    calories += 431
elif burger == 3:
    calories += 420

if side == 1:
    calories += 100
elif side == 2:
    calories += 57
elif side == 3:
    calories += 70
    
if drink == 1:
    calories += 130
elif drink == 2:
    calories += 160
elif drink == 3:
    calories += 118
    
if dessert == 1:
    calories += 167
elif dessert == 2:
    calories += 266
elif dessert == 3:
    calories += 75

print('Your total Calorie count is %s.' % calories)