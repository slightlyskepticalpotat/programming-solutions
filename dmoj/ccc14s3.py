for i in range(0,int(input())):
    main_line, branch = [], []
    counter = 1
    
    for i in range(0,int(input())):
        main_line.append(int(input()))
    main_line = main_line[::-1]

    for elem in main_line:
        if elem == counter:
            counter+=1
        else:
            branch.append(elem)
        for i in range(0, len(branch)):
            if branch[-1] == counter:
                branch.pop()
                counter+=1
            else:
                break
            
    if branch == []:
        print('Y')
    else:
        print('N')