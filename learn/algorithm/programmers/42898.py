def solution(m, n, puddles):
    for i in range(len(puddles)):
        puddles[i][0], puddles[i][1] = puddles[i][0] - 1, puddles[i][1] - 1
    answer = [[0] * m for _ in range(n)]
    answer[0][0] = 1
    for i in range(n):
        for j in range(m):
            if [j, i] in puddles:
                answer[i][j] = 0
                continue
            if i > 0 and j > 0:
                answer[i][j] = (answer[i][j - 1] + answer[i - 1][j]) % 1000000007
            elif i > 0:
                answer[i][j] = answer[i - 1][j]
            elif j > 0:
                answer[i][j] = answer[i][j - 1]
    return answer[-1][-1]
