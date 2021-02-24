import sys

input = sys.stdin.readline

events, order, stack, flag = [input().strip() for _ in range(int(input()) * 2)][::-1], [], [], True
for event in events: # work backwards, stack is what we need to add
    if event[0] == "+": # we remove an element
        if not stack:
            flag = False
            break
        order.append(stack.pop())
    else: # we add an element
        p = int(event[2:])
        if stack and stack[-1] < p:
            flag = False
            break
        stack.append(p)
if flag:
    print("YES")
    print(*order[::-1])
else:
    print("NO")
