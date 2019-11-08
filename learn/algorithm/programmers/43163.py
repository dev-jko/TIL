answer = None


def solution(begin, target, words):
    global answer
    answer = len(words) + 1
    dfs(0, begin, [False] * len(words), target, words)
    return answer if answer != len(words) + 1 else 0


def check(current, word):
    cnt = 0
    for i in range(len(word)):
        if current[i] != word[i]:
            cnt += 1
        if cnt > 1:
            return False
    return True


def dfs(k, current, used, target, words):
    global answer
    if current == target:
        answer = k
    else:
        if k + 1 >= answer:
            return
        for i in range(len(words)):
            if not used[i] and check(current, words[i]):
                used[i] = True
                dfs(k + 1, words[i], used, target, words)
                used[i] = False


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
# 4
