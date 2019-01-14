# TODO 시간초과

from sys import stdin
n = int(stdin.readline())
inputs = []
for _ in range(n):
    inputs.append(int(stdin.readline()))
stack = [1]
i = 1
result = '+\n'
while len(inputs) > 0:
    if len(stack) == 0 or stack[-1] < inputs[0]:
        i += 1
        stack.append(i)
        result += '+\n'
    elif stack[-1] == inputs[0]:
        result += '-\n'
        inputs = inputs[1:]
        stack.pop()
    else:
        result = 'NO'
        break
print(result)
