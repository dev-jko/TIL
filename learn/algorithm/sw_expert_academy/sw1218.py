BRACKETS = {
    'start': '([{<',
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
for T in range(1, 11):
    N = int(input())
    string = input()
    stack = []
    result = 1
    for c in string:
        if c in BRACKETS['start']:
            stack.append(c)
        else:
            if len(stack) > 0:
                out = stack.pop(-1)
                if BRACKETS[c] != out:
                    result = 0
                    break
            else:
                result = 0
                break
    else:
        if len(stack) > 0:
            result = 0
    print(f'#{T} {result}')
