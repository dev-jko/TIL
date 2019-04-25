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
        if nxy in self.body:
            return False
        self.body.appendleft(nxy)
        if nxy in apple:
            self.size += 1
            apple.remove(nxy)
        else:
            self.body.pop()
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
print(t)

# from collections import deque
#
# dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# N = int(input())
# apple = set()
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     apple.add((a - 1, b - 1))
# data = {}
# for _ in range(int(input())):
#     a, b = input().split()
#     data[int(a)] = b
# body = deque()
# body.append((0, 0))
# d = 1
# t = 0
# while True:
#     t += 1
#     check = True
#     head = body.popleft()
#     body.appendleft(head)
#     nxy = (head[0] + dxy[d][0], head[1] + dxy[d][1])
#     if nxy[0] < 0 or nxy[0] >= N or nxy[1] < 0 or nxy[1] >= N or nxy in body:
#         check = False
#     else:
#         body.appendleft(nxy)
#         if nxy in apple:
#             apple.remove(nxy)
#         else:
#             body.pop()
#     if not check:
#         break
#     if t in data:
#         if data[t] == 'D':
#             d = (d + 1) % 4
#         else:
#             d = (d + 3) % 4
# print(t)
