tines_height = int(input())
tines_spacing = int(input())
handle_length = int(input())

for i in range(0,tines_height):
    print('*',(tines_spacing-2)*' ','*',(tines_spacing-2)*' ','*')

print((tines_spacing*2+3)*'*')

for i in range(0, handle_length):
    print((tines_spacing)*' ', '*')