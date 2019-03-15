# 4014. [모의 SW 역량테스트] 활주로 건설

def check(arr):
    is_used = [False for _ in range(N)]
    leng = 1
    for i in range(N - 1):
        if arr[i] == arr[i + 1]:
            leng += 1
        elif arr[i] + 1 == arr[i + 1]:
            if leng < X:
                return 0
            for j in range(i - X + 1, i + 1):
                is_used[j] = True
            leng = 1
        elif arr[i] == arr[i + 1] + 1:
            leng = 1
            continue
        else:
            return 0
    leng = 1
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == arr[i - 1]:
            leng += 1
        elif arr[i] + 1 == arr[i - 1]:
            if leng < X:
                return 0
            for j in range(i, i + X):
                if is_used[j]:
                    return 0
                is_used[j] = True
            leng = 1
        elif arr[i] == arr[i - 1] + 1:
            leng = 1
            continue
        else:
            return 0
    return 1


for T in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    data = []
    data_t = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        data.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(N):
            data_t[j][N - i - 1] = data[i][j]
    result = 0
    for i in range(N):
        result += check(data[i]) + check(data_t[i])
    print('#{} {}'.format(T, result))
