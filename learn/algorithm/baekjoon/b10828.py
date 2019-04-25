import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    else:
        if cmd[0] == 'pop':
            output = stack.pop() if len(stack) > 0 else -1
        elif cmd[0] == 'size':
            output = len(stack)
        elif cmd[0] == 'empty':
            output = 0 if len(stack) > 0 else 1
        else:
            output = stack[-1] if len(stack) > 0 else -1
        print(output)
