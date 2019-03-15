# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기


N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(input())
result = 99999
is_end = False
for i in range(N - 7):
    for j in range(M - 7):
        for s in ['B', 'W']:
            cnt = 0
            t = s
            for x in range(i, i + 8):
                t = 'B' if t == 'W' else 'W'
                for y in range(j, j + 8):
                    t = 'B' if t == 'W' else 'W'
                    if t != data[x][y]:
                        cnt += 1
            result = min(result, cnt)
            if result == 0:
                is_end = True
                break
        if is_end:
            break
    if is_end:
        break
print(result)
