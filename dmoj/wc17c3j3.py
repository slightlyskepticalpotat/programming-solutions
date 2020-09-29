password = input().strip()
if 8 <= len(password) <= 12:
    if sum([1 for char in password if char.islower()]) >= 3:
        if sum([1 for char in password if char.isupper()]) >= 2:
            if sum([1 for char in password if char.isdigit()]) >= 1:
                print("Valid")
                raise SystemExit
print("Invalid")