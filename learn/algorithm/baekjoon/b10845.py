from sys import stdin

N = int(stdin.readline())
queue = []
for _ in range(N):
    used = stdin.readline().split()
    if used[0] == 'push':
        queue.insert(0, used[1])
    else:
        if used[0] == 'pop':
            output = queue.pop() if len(queue) > 0 else -1
        elif used[0] == 'size':
            output = len(queue)
        elif used[0] == 'empty':
            output = 1 if len(queue) < 1 else 0
        elif used[0] == 'front':
            output = queue[-1] if len(queue) > 0 else -1
        else:
            output = queue[0] if len(queue) > 0 else -1
        print(output)
