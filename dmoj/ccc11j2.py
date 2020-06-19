h = int(input())
m = int(input())
sw = 0

for i in range(1,m):
    if (-6*i**4 + h*i**3 + 2*i**2 + i) <= 0:
        print('The balloon first touches ground at hour:')
        print(i)
        sw = 1
        break
    else:
        pass
if sw == 0:
    print('The balloon does not touch ground in the given time.')