# https://www.acmicpc.net/problem/17070
# 파이프 옮기기 1


# 상태 0 가로, 1세로, 2대각
N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
result = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
result[0][1][0] = 1
for i in range(N):
    for j in range(1, N):
        if i == 0 and j == 1:
            continue
        if data[i][j] == 0:
            result[i][j][0] = result[i][j - 1][0] + result[i][j - 1][2]
            if i > 0:
                result[i][j][1] = result[i - 1][j][1] + result[i - 1][j][2]
                if data[i - 1][j] == 0 and data[i][j - 1] == 0:
                    result[i][j][2] = result[i - 1][j - 1][0] + result[i - 1][j - 1][1] + result[i - 1][j - 1][2]
print(sum(result[N - 1][N - 1]))



# def dfs(x, y, state):
#     if x == N - 1 and y == N - 1:
#         global result
#         result += 1
#     else:
#         # 가로 상태
#         if state == 0:
#             nx, ny = x, y + 1
#             if nx < N and ny < N and data[nx][ny] == 0:
#                 dfs(nx, ny, 0)
#             nx, ny = x + 1, y + 1
#             if nx < N and ny < N and data[nx][ny] == 0:
#                 tx1, ty1 = x, y + 1
#                 tx2, ty2 = x + 1, y
#                 if data[tx1][ty1] == 0 and data[tx2][ty2] == 0:
#                     dfs(nx, ny, 2)
#         # 세로 상태
#         elif state == 1:
#             nx, ny = x + 1, y
#             if nx < N and ny < N and data[nx][ny] == 0:
#                 dfs(nx, ny, 1)
#             nx, ny = x + 1, y + 1
#             if nx < N and ny < N and data[nx][ny] == 0:
#                 tx1, ty1 = x, y + 1
#                 tx2, ty2 = x + 1, y
#                 if data[tx1][ty1] == 0 and data[tx2][ty2] == 0:
#                     dfs(nx, ny, 2)
#         # 대각 상태
#         elif state == 2:
#             nx, ny = x, y + 1
#             if nx < N and ny < N and data[nx][ny] == 0:
#                 dfs(nx, ny, 0)
#             nx, ny = x + 1, y
#             if nx < N and ny < N and data[nx][ny] == 0:
#                 dfs(nx, ny, 1)
#             nx, ny = x + 1, y + 1
#             if nx < N and ny < N and data[nx][ny] == 0:
#                 tx1, ty1 = x, y + 1
#                 tx2, ty2 = x + 1, y
#                 if data[tx1][ty1] == 0 and data[tx2][ty2] == 0:
#                     dfs(nx, ny, 2)
#
#
# # 상태 0 가로, 1세로, 2대각
# N = int(input())
# data = []
# for _ in range(N):
#     data.append(list(map(int, input().split())))
# result = 0
# dfs(0, 1, 0)
# print(result)
