place = list(input())
place2 = []
for i in range(0,len(place)):
    if place[i] == 'a' or place[i] == 'e' or place[i] == 'i' or place[i] == 'o' or place[i] == 'u':
        place2.append(place[i])
    elif place[i] == 'b':
        place2.append(place[i] + 'a' + 'c')
    elif place[i] == 'c':
        place2.append(place[i] + 'a' + 'd')
    elif place[i] == 'd':
        place2.append(place[i] + 'e' + 'f')
    elif place[i] == 'f':
        place2.append(place[i] + 'e' + 'g')
    elif place[i] == 'g':
        place2.append(place[i] + 'e' + 'h')
    elif place[i] == 'h':
        place2.append(place[i] + 'i' + 'j')
    elif place[i] == 'j':
        place2.append(place[i] + 'i' + 'k')
    elif place[i] == 'k':
        place2.append(place[i] + 'i' + 'l')
    elif place[i] == 'l':
        place2.append(place[i] + 'i' + 'm')
    elif place[i] == 'm':
        place2.append(place[i] + 'o' + 'n')
    elif place[i] == 'n':
        place2.append(place[i] + 'o' + 'p')
    elif place[i] == 'p':
        place2.append(place[i] + 'o' + 'q')
    elif place[i] == 'q':
        place2.append(place[i] + 'o' + 'r')
    elif place[i] == 'r':
        place2.append(place[i] + 'o' + 's')
    elif place[i] == 's':
        place2.append(place[i] + 'u' + 't')
    elif place[i] == 't':
        place2.append(place[i] + 'u' + 'v')
    elif place[i] == 'v':
        place2.append(place[i] + 'u' + 'w')
    elif place[i] == 'w':
        place2.append(place[i] + 'u' + 'x')
    elif place[i] == 'y':
        place2.append(place[i] + 'u' + 'z')
    elif place[i] == 'z':
        place2.append(place[i] + 'u' + 'z')

print(''.join(place2))