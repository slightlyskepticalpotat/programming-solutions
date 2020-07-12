import textwrap

flag = 0
for i in range(10):
    line_limit = int(input())
    text = input().strip()
    
    wrapped = textwrap.wrap(text, line_limit, break_long_words=False)
    for i in range(len(wrapped)):
        if len(wrapped[i]) <= line_limit and flag == 0:
            print(wrapped[i])
        elif flag == 0: # break word across line
            flag = 0
            placeholder = []
            while wrapped[i]:
                placeholder.append(wrapped[i][:line_limit])
                wrapped[i] = wrapped[i][line_limit:]
            try:
                if len(placeholder[-1]) + len(wrapped[i+1]) < line_limit:
                    placeholder[-1] = str(placeholder[-1] + " " + wrapped[i+1])
                    flag = 1
            except:
                pass
            for thing in placeholder:
                print(thing)
        else:
            flag = 0
    print("=====")