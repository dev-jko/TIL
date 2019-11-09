from heapq import heappush, heappop
def solution(n, edge):
    adj = [False, *([] for _ in range(n))]
    for s, e in edge:
        adj[s].append(e)
        adj[e].append(s)
    result = [-1] * (n + 1)
    visited = [False] * (n + 1)
    visited[1] = True
    h = [(0, 1)]
    while h:
        d, node = heappop(h)
        for next in adj[node]:
            if not visited[next] and (result[next] == -1 or result[next] > d + 1):
                result[next] = d + 1
                visited[next] = True
                heappush(h, (d + 1, next))
    return result.count(max(result))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
# 3
