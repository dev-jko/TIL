# 4008. [모의 SW 역량테스트] 숫자 만들기


def dfs(k, result):
    if k == N - 1:
        global min_result, max_result
        min_result = min(min_result, result)
        max_result = max(max_result, result)
    else:
        if operator[0] > 0:
            operator[0] -= 1
            dfs(k + 1, result + data[k + 1])
            operator[0] += 1
        if operator[1] > 0:
            operator[1] -= 1
            dfs(k + 1, result - data[k + 1])
            operator[1] += 1
        if operator[2] > 0:
            operator[2] -= 1
            dfs(k + 1, result * data[k + 1])
            operator[2] += 1
        if operator[3] > 0:
            operator[3] -= 1
            if result < 0:
                dfs(k + 1, -(-result // data[k + 1]))
            else:
                dfs(k + 1, result // data[k + 1])
            operator[3] += 1


for T in range(1, int(input()) + 1):
    N = int(input())
    operator = list(map(int, input().split()))
    data = list(map(int, input().split()))
    min_result = 0xffffffff
    max_result = -0xffffffff
    dfs(0, data[0])
    print('#{} {}'.format(T, max_result - min_result))
