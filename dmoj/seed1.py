text = input()
ree = 0
if 'B' not in text:
    print('B')
    ree += 1
if 'F' not in text:
    print('F')
    ree += 1
if 'T' not in text:
    print('T')
    ree += 1
if 'L' not in text:
    print('L')
    ree += 1
if 'C' not in text:
    print('C')
    ree += 1
if ree == 0:
    print('NO MISSING PARTS')