for T in range(1, int(input()) + 1):
    inputs = list(input().split())
    stack = []
    check = True
    for c in inputs:
        if c == '.':
            break
        if c not in ['+', '*', '-', '/']:
            stack.append(int(c))
        elif len(stack) >= 2:
            if c == '+':
                stack.append(stack.pop(-2) + stack.pop())
            elif c == '*':
                stack.append(stack.pop(-2) * stack.pop())
            elif c == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif c == '/':
                stack.append(stack.pop(-2) // stack.pop())
        else:
            check = False
            break
    if len(stack) != 1 or not check:
        result = 'error'
    else:
        result = stack.pop()
    print(f'#{T} {result}')
