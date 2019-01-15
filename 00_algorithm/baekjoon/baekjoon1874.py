from sys import stdin
n = int(stdin.readline())
inputs = []
for _ in range(n):
    inputs.append(int(stdin.readline()))
stack = [1]
i = 1
top = 0
index = 0
result = ['+']
while i <= n:
    if top < 0 or stack[top] < inputs[index]:
        i += 1
        stack.append(i)
        result.append('+')
        top += 1
    elif stack[top] == inputs[index]:
        result.append('-')
        index += 1
        stack.pop()
        top -= 1
    else:
        result = ['NO', None]
        break
result = result[:-1]
print(*result, sep="\n")
