import math

c = float(input().strip())
days = math.ceil(365 * 2 * math.log(c / 2, 2))
if days == 0:
    print("Now!")
else:
    if days >= 365:
        print(f"{days // 365}Y", end = " ")
        days -= (365 * (days // 365))
    if days >= 30:
        print(f"{days // 30}M", end = " ")
        days -= (30 * (days // 30))
    if days >= 7:
        print(f"{days // 7}W", end = " ")
        days -= (7 * (days // 7))
    if days >= 1:
        print(f"{days // 1}D", end = " ")
        days -= (1 * (days // 1))