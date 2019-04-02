# 1952. [모의 SW 역량테스트] 수영장


def dfs(k, em, total_fee):
    global result
    if k == 12:
        result = min(result, total_fee)
    else:
        if total_fee >= result:
            return
        if k <= em:
            dfs(k + 1, em, total_fee)
            dfs(k + 1, k + 2, total_fee + fee[2])  # 3달 이용권
        else:
            dfs(k + 1, 0, total_fee + fee[0] * plan[k])  # 1일 이용권
            dfs(k + 1, 0, total_fee + fee[1])  # 1달 이용권
            dfs(k + 1, k + 2, total_fee + fee[2])  # 3달 이용권


for T in range(1, int(input()) + 1):
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    result = fee[-1]
    dfs(0, -1, 0)
    print('#{} {}'.format(T, result))
