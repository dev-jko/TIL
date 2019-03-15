# 2112. [모의 SW 역량테스트] 보호 필름


def bt(k, cnt):
    global result
    if result == 0:
        return
    if k == D:
        for i in range(W):
            count = 1
            t = data[0][i]
            for j in range(1, D):
                if t == data[j][i]:
                    count += 1
                    if count >= K:
                        break
                else:
                    t = data[j][i]
                    count = 1
            if count < K:
                return
        result = min(result, cnt)
    else:
        for j in range(W):
            data[k][j] = inputs[k][j]
        bt(k + 1, cnt)
        if cnt + 1 < result or result == 99999:
            for j in range(W):
                data[k][j] = 0
            bt(k + 1, cnt + 1)
            for j in range(W):
                data[k][j] = 1
            bt(k + 1, cnt + 1)


ans = []
for T in range(1, int(input()) + 1):
    D, W, K = map(int, input().split())
    inputs = []
    for _ in range(D):
        inputs.append(list(map(int, input().split())))
    data = [[0 for _ in range(W)] for _ in range(D)]
    result = 99999
    use = [2 for _ in range(D)]
    bt(0, 0)
    ans.append('#{} {}'.format(T, result))
for an in ans:
    print(an)
