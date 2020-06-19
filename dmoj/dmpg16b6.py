# https://dmoj.ca/problem/dmpg16b6
import sys
input = sys.stdin.readline

ops = int(input())

for i in range(0, ops):
    remainder = 0
    instruction = input()
    convert = instruction[0:1]
    number = int(instruction[2:].strip())
    result = 0
    
    if convert == 'A':
        counter = 0
        number = [int(i) for i in str(number)]
        while number:
            result += int(number.pop())*pow(-2, counter)
            counter += 1
        print(result)
    else:
        result = []
        if number == 0:
            print(0)
        else:
            while number != 0:
                number, remainder = divmod(number, -2)
                if remainder < 0:
                    number+=1
                    remainder + 2
                result.append(str(remainder))
        print(''.join(result)[::-1].replace("-",""))