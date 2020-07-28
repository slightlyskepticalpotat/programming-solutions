n = int(input())

print(n * "*") # top
for i in range(1, (n - 3) + 1 , 2):
    print((n - i)//2 * "*" + i * " " + (n - i)//2 * "*")
print("*" + " " * (n - 2) + "*") # middle
for i in range((n - 3) - 1 , -1, -2):
    print((n - i)//2 * "*" + i * " " + (n - i)//2 * "*")
print(n * "*") # bottom