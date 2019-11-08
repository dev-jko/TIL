answer = []


def solution(tickets):
    global answer
    answer = []
    dfs(0, len(tickets), [False] * len(tickets), ["ICN"], tickets)
    answer.sort()
    return answer[0]


def dfs(k, N, used, path, tickets):
    if k == N:
        answer.append(path[:])
    else:
        for i in range(len(tickets)):
            if used[i] or tickets[i][0] != path[-1]:
                continue
            used[i] = True
            path.append(tickets[i][1])
            dfs(k + 1, N, used, path, tickets)
            used[i] = False
            path.pop()


print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
