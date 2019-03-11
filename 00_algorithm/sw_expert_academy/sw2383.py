# swea 2383. [모의 SW 역량테스트] 점심 식사시간

# TODO 실패


# 6 45
# 7 50


from collections import deque


def get_time(p, s):
    return abs(p[0] - s[0]) + abs(p[1] - s[1])

def compare_ps(ps):
    return ps['p']

def dfs(k, n):
    global result
    if k == n:
        S = [[[],[]], [[],[]]]
        for i in range(n):
            if select[i] == 0:
                S[0][0].append({'p': P[i][0], 's': s[0][1]})
            else:
                S[1][0].append({'p': P[i][1], 's': s[1][1]})
        S[0][0].sort(key=compare_ps, reverse=True)
        S[1][0].sort(key=compare_ps, reverse=True)
        if len(S[0]) == 0:
            t = S[1][0][-1]['p']
        elif len(S[1]) == 0:
            t = S[0][0][-1]['p']
        else:
            t = min(S[0][0][-1]['p'], S[1][0][-1]['p'])
        for i in range(2):
            j = 0
            while j < len(S[i][0]):
                S[i][0][j]['p'] -= t
                if S[i][0][j]['p'] == 0:
                    S[i][1].append(S[i][0].pop(j))
                else:
                    j += 1
        while len(S[0][0]) + len(S[0][1]) and len(S[1][0]) + len(S[1][1]):
            t += 1
            for i in S[0][0]:
                if i['p'] == 0:
                    S
                if S[0]

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
    # 1 사람, 2 이상 계단 입구, 길이
    # p[사람번호][x, y]
    # s[계단번호][좌표, 길이]
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
