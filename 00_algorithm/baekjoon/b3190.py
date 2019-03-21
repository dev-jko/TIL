# https://www.acmicpc.net/problem/3190
# 뱀


from collections import deque

class Snake:
    def __init__(self):
        self.body = deque()
        self.body.append((0, 0))
        self.d = 1
        self.size = 1

    def turn(self, cmd):
        if cmd == 'D':
            self.d = (self.d + 1) % 4
        elif cmd == 'L':
            self.d = (self.d + 3) % 4

    def move(self):
        head = self.body.popleft()
        self.body.appendleft(head)
        nxy = (head[0] + dxy[self.d][0], head[1] + dxy[self.d][1])
        if nxy[0] < 0 or nxy[0] >= N or nxy[1] < 0 or nxy[1] >= N:
            return False
        if nxy in apple:
            self.size += 1
            apple.remove(nxy)
        else:
            self.body.pop()
        if nxy in self.body:
            return False
        self.body.appendleft(nxy)
        return True


dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N = int(input())
K = int(input())
apple = set()
for _ in range(K):
    a, b = map(int, input().split())
    apple.add((a - 1, b - 1))
l = int(input())
data = {}
for _ in range(l):
    a, b = input().split()
    data[int(a)] = b

snake = Snake()
t = 0
while True:
    t += 1


    if not snake.move():
        break
    if t in data:
        snake.turn(data[t])


    test = [[0 for _ in range(N)] for _ in range(N)]
    for x, y in snake.body:
        test[x][y] = 1
    for arrtt in test:
        print(arrtt)
    print(t)


print(t)
