result = False

total = input()

true = int(total.count("True"))
false = int(total.count("False"))

if true == 1:
    result = True
else:
    pass

times_not = int(total.count("not"))

for i in range(0,times_not):
    result = not result

print(result)