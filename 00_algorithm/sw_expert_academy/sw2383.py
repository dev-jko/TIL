# swea 2383. [모의 SW 역량테스트] 점심 식사시간


def get_time(p, s):
    return abs(p[0] - s[0]) + abs(p[1] - s[1])


def compare_p(ps):
    return ps['p']


def compare_s(ps):
    return ps['s']


def dfs(k, n):
    global result
    if k == n:
        S = [[[], []], [[], []]]
        for i in range(n):
            if select[i] == 0:
                S[0][0].append({'p': P[i][0] + 1, 's': s[0][1]})
            else:
                S[1][0].append({'p': P[i][1] + 1, 's': s[1][1]})
        S[0][0].sort(key=compare_p)
        S[1][0].sort(key=compare_p)
        t = 0
        while len(S[0][0]) + len(S[0][1]) or len(S[1][0]) + len(S[1][1]):
            t += 1
            for i in S[0][0]:
                i['p'] -= 1
            for i in S[1][0]:
                i['p'] -= 1
            for i in range(len(S[0][1]) if len(S[0][1]) < 3 else 3):
                S[0][1][i]['s'] -= 1
            for i in range(len(S[1][1]) if len(S[1][1]) < 3 else 3):
                S[1][1][i]['s'] -= 1
            S[0][0].sort(key=compare_p)
            S[1][0].sort(key=compare_p)
            S[0][1].sort(key=compare_s)
            S[1][1].sort(key=compare_s)
            if len(S[0][0]) != 0:
                temp = S[0][0][0]
                while temp['p'] <= 0:
                    S[0][1].append(S[0][0].pop(0))
                    if len(S[0][0]) == 0:
                        break
                    temp = S[0][0][0]
            if len(S[0][1]) != 0:
                temp = S[0][1][0]
                while temp['s'] <= 0:
                    S[0][1].pop(0)
                    if len(S[0][1]) == 0:
                        break
                    temp = S[0][1][0]
            if len(S[1][0]) != 0:
                temp = S[1][0][0]
                while temp['p'] <= 0:
                    S[1][1].append(S[1][0].pop(0))
                    if len(S[1][0]) == 0:
                        break
                    temp = S[1][0][0]
            if len(S[1][1]) != 0:
                temp = S[1][1][0]
                while temp['s'] <= 0:
                    S[1][1].pop(0)
                    if len(S[1][1]) == 0:
                        break
                    temp = S[1][1][0]
        result = min(result, t)
    else:
        select[k] = 0
        dfs(k + 1, n)
        select[k] = 1
        dfs(k + 1, n)


for T in range(1, int(input()) + 1):
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    p = []
    s = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                p.append((i, j))
            if data[i][j] > 1:
                s.append(((i, j), data[i][j]))
    P = []
    for i in p:
        temp = []
        for j in s:
            temp.append(get_time(i, j[0]))
        P.append(temp)
    select = [0 for _ in range(len(P))]
    result = 9999999
    dfs(0, len(P))
    print('#{} {}'.format(T, result))
