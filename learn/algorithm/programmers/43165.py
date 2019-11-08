answer = 0


def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, len(numbers), [1] * len(numbers), numbers, target)
    return answer


def dfs(k, N, operators, numbers, target):
    if k == N:
        global answer
        s = 0
        for i in range(len(operators)):
            s += operators[i] * numbers[i]
        if s == target:
            answer += 1
    else:
        operators[k] = 1
        dfs(k + 1, N, operators, numbers, target)
        operators[k] = -1
        dfs(k + 1, N, operators, numbers, target)


print(solution([1, 1, 1, 1, 1], 3))
# 5
