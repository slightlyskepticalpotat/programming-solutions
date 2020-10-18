for i in range(10):
    expression = [char for char in input().strip().replace("(", "").replace(")", "").replace("q", "//").replace("r", "%").split()][::-1] # brackets aren't needed in prefix or postfix notation
    stack = [] # fake stack
    for token in expression:
        if token in ["+", "-", "*", "//", "%"]:
            a, b = stack.pop(), stack.pop()
            if token == "//" and int(a) < 0 and int(b) > 0 and not int(a) / int(b) == int(a) // int(b): # floor division doesn't work properly when negative // positive with remainder
                stack.append(str(eval(a + token + b) + 1))
            else:
                stack.append(str(eval(a + token + b)))
        else:
            stack.append(token)
    print(stack[0])