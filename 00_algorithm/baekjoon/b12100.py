# https://www.acmicpc.net/problem/12100
# 2048 (Easy)

from collections import deque
from itertools import product


def left(data):
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                q.append(data[i][j])
        data[i][0] = q.popleft() if q else 0
        for j in range(1, N):
            if q:
                t = q.popleft()
                if t == data[i][j - 1]:
                    data[i][j - 1] += t
                    data[i][j] = q.popleft() if q else 0
                else:
                    data[i][j] = t
            else:
                data[i][j] = 0


def right(data):
    for i in range(N):
        for j in range(N - 1, -1, -1):
            if data[i][j] != 0:
                q.append(data[i][j])
        data[i][N - 1] = q.popleft() if q else 0
        for j in range(N - 2, -1, -1):
            if q:
                t = q.popleft()
                if t == data[i][j + 1]:
                    data[i][j + 1] += t
                    data[i][j] = q.popleft() if q else 0
                else:
                    data[i][j] = t
            else:
                data[i][j] = 0


def up(data):
    for i in range(N):
        for j in range(N):
            if data[j][i] != 0:
                q.append(data[j][i])
        data[0][i] = q.popleft() if q else 0
        for j in range(1, N):
            if q:
                t = q.popleft()
                if t == data[j - 1][i]:
                    data[j - 1][i] += t
                    data[j][i] = q.popleft() if q else 0
                else:
                    data[j][i] = t
            else:
                data[j][i] = 0


def down(data):
    for i in range(N):
        for j in range(N - 1, -1, -1):
            if data[j][i] != 0:
                q.append(data[j][i])
        data[N - 1][i] = q.popleft() if q else 0
        for j in range(N - 2, -1, -1):
            if q:
                t = q.popleft()
                if t == data[j + 1][i]:
                    data[j + 1][i] += t
                    data[j][i] = q.popleft() if q else 0
                else:
                    data[j][i] = t
            else:
                data[j][i] = 0


def get_max(data):
    result = 0
    for arr in data:
        result = max(result, *arr)
    return result


N = int(input())
data = []
q = deque()
for _ in range(N):
    data.append(list(map(int, input().split())))
move = [up, down, left, right]
result = 0
for perm in product(move, repeat=5):
    temp = [[i for i in j] for j in data]
    for func in perm:
        func(temp)
    result = max(result, get_max(temp))
print(result)
