cases = int(input())
numbers = []

for i in range(0,cases):
    holder = int(input())
    if holder == 0:
        numbers.pop()
    else:
        numbers.append(holder)
        
print(sum(numbers))