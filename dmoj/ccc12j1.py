limit = int(input())
speed = int(input())
difference = speed-limit

if difference <= 0:
    print('Congratulations, you are within the speed limit!')
elif 1 <= difference <= 20:
    print('You are speeding and your fine is $100.')
elif 21 <= difference <= 30:
    print('You are speeding and your fine is $270.')
else:
    print('You are speeding and your fine is $500.')