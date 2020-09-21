n, more_than_perfect = int(input()), 0
name = input()
for _ in range(n):
    paper = input()
    try: 
        a, b = paper.split()
        a = eval(a) 
    except: # no name
        try: 
            if "/" not in paper: # cut off
                paper += "0"
            a = eval(paper)
        except: # no n
            a = int(paper[:-1]) 
        b = ""
    if name.startswith(b) and a > 1:
        print("Y")
    else:
        print("N")