answer = None


def solution(n, computers):
    global answer
    answer = dict()
    used = [False] * n
    for i in range(n):
        if used[i]:
            continue
        answer[i] = set()
        dfs(i, i, used, n, computers)
    return len(answer)


def dfs(start, current, used, n, computers):
    global answer
    for i in range(n):
        if used[i] or computers[current][i] == 0:
            continue
        answer[start].add(i)
        used[i] = True
        dfs(start, i, used, n, computers)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1
