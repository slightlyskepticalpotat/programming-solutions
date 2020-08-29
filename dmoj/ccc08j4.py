while True:
    prefix = [i for i in input().split()][::-1]
    operators, postfix = [], []
    if prefix == ["0"]:
        break

    for i in prefix:
        if i in ["+", "-"]: # operator
            a, b = postfix.pop(), postfix.pop()
            postfix.append(a + b + i)
        else: # operand
            postfix.append(i)
    print(*[i for i in postfix[0]])