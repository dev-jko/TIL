PRIORITY = {
    'in': {'(': 3, '*': 2, '+': 1},
    'out': {'(': 0, '*': 2, '+': 1}
}

for T in range(1, 11):
    input()
    stack = []
    temp = []
    for c in input():
        if c in ['(', ')', '*', '+']:
            if len(stack) == 0:
                stack.append(c)
            else:
                if c == ')':
                    top = stack.pop()
                    while top != '(':
                        temp.append(top)
                        top = stack.pop()
                elif PRIORITY['out'][stack[-1]] >= PRIORITY['in'][c]:
                    temp.append(stack.pop())
                    stack.append(c)
                else:
                    stack.append(c)
        else:
            temp.append(int(c))
    for v in temp:
        if v in ['*', '+']:
            if v == '+':
                stack.append(stack.pop(-2) + stack.pop())
            else:
                stack.append(stack.pop(-2) * stack.pop())
        else:
            stack.append(v)
    print(f'#{T} {stack.pop()}')
