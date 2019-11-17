answer = 0


def solution(numbers, target):
    global answer
    dfs(0, len(numbers), numbers, target)
    return answer


def dfs(k, N, numbers, target):
    global answer
    if k == N:
        if sum(numbers) == target:
            answer += 1
        return
    numbers[k] = -numbers[k]
    dfs(k + 1, N, numbers, target)
    numbers[k] = -numbers[k]
    dfs(k + 1, N, numbers, target)
