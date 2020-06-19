import sys
input = sys.stdin.readline
response = 'YES'

number = int(input())
ren = int(input())

for i in range(1,number):
    if ren > int(input()):
        pass
    else:
        response = 'NO'
        
print(response)