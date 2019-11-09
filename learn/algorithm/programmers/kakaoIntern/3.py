def solution(user_id, banned_id):
    ban = []
    for b_id in banned_id:
        ban.append([])
        for u_id in user_id:
            if len(b_id) != len(u_id):
                continue
            for i in range(len(u_id)):
                if b_id[i] != u_id[i] and b_id[i] != '*':
                    break
            else:
                ban[-1].append(u_id)
    global answer
    answer = set()
    used = [False] * len(user_id)
    dfs(0, len(ban), used, user_id, ban)
    return len(answer)


def dfs(k, N, used, user_id, ban):
    if k == N:
        global answer
        answer.add(tuple(used))
    else:
        for i in range(len(user_id)):
            if used[i]:
                continue
            if user_id[i] in ban[k]:
                used[i] = True
                dfs(k + 1, N, used, user_id, ban)
                used[i] = False



inputs = [
    [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]], #	2
    [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]], #	2
    [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]] #	3
]
for input123123 in inputs:
    print(solution(*input123123))
