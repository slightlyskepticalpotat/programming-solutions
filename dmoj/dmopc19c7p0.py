import sys
input= sys.stdin.readline
data = [int(i) for i in input().strip().split()]
def avg(a, b):
    return (a+b)/2

print(avg(data[0], data[1]))
print(avg(data[0], data[2]))
print(avg(data[0], data[3]))
print(avg(data[1], data[2]))
print(avg(data[1], data[3]))
print(avg(data[2], data[3]))
print((data[0]+data[1]+data[2])/3)
print((data[0]+data[1]+data[3])/3)
print((data[0]+data[2]+data[3])/3)
print((data[1]+data[2]+data[3])/3)
print((data[0]+data[1]+data[2]+data[3])/4)