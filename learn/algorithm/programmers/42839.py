def solution(numbers):
    s = set()
    dfs(0, "", [False] * len(numbers), numbers, s)
    s = s - {0, 1}
    answer = len(s)
    return answer


def dfs(k, num, used, numbers, s):
    if k == len(numbers):
        if num == "":
            return
        i = int(num)
        if check(i):
            s.add(i)
    else:
        dfs(k + 1, num, used, numbers, s)
        for i in range(len(numbers)):
            if not used[i]:
                used[i] = True
                dfs(k + 1, num + numbers[i], used, numbers, s)
                used[i] = False


def check(num):
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True
