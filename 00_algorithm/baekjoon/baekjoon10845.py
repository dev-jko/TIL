from sys import stdin

N = int(stdin.readline())
queue = []
for _ in range(N):
    cmd = stdin.readline().split()
    if cmd[0] == 'push':
        queue.insert(0, cmd[1])
    else:
        if cmd[0] == 'pop':
            output = queue.pop() if len(queue) > 0 else -1
        elif cmd[0] == 'size':
            output = len(queue)
        elif cmd[0] == 'empty':
            output = 1 if len(queue) < 1 else 0
        elif cmd[0] == 'front':
            output = queue[-1] if len(queue) > 0 else -1
        else:
            output = queue[0] if len(queue) > 0 else -1
        print(output)
