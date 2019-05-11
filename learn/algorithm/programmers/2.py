def dfs(n, open, close, string, answer):
    if open == close == n:
        answer.append(string)
    else:
        if open < n:
            dfs(n, open + 1, close, string + '(', answer)
            if open > close:
                dfs(n, open, close + 1, string + ')', answer)
        elif close < open:
            dfs(n, open, close + 1, string + ')', answer)


def solution(N):
    answer = []
    dfs(N, 0, 0, '', answer)
    return answer


for i in range(4, 5):
    print(*solution(i), sep='\n')
    print()
