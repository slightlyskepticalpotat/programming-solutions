cases = int(input())

def sep(string, length):
    return ' '.join(string[i:i+length] for i in range(0,len(string),length))

for i in range(0,cases):
    #raw binary in string format
    binary = (str(bin(int(input()))[2:]))
    
    if len(binary) % 4 != 0:
        
        binary = (4 - (len(binary) % 4))*'0' + binary
        
    print(sep(binary,4))