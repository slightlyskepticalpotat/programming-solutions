conversion = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
aromantic, decimal = input().strip(), 0
aromantic = [list(aromantic[i:i+2]) for i in range(0, len(aromantic), 2)]

for i in range(len(aromantic) - 1): # everything except last element
    if list(conversion.keys()).index(aromantic[i][1]) >= list(conversion.keys()).index(aromantic[i+1][1]):
        decimal += (int(aromantic[i][0]) * conversion[aromantic[i][1]])
    else:
        decimal -= (int(aromantic[i][0]) * conversion[aromantic[i][1]])
decimal += (int(aromantic[-1][0]) * conversion[aromantic[-1][1]])
print(decimal)