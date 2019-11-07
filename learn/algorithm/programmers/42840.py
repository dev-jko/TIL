a1 = [1, 2, 3, 4, 5] * (10000 // 5)
a2 = [2, 1, 2, 3, 2, 4, 2, 5] * (10000 // 8)
a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000 // 10)


def solution(answers):
    answer = [0, 0, 0]
    for i in range(len(answers)):
        if a1[i] == answers[i]:
            answer[0] += 1
        if a2[i] == answers[i]:
            answer[1] += 1
        if a3[i] == answers[i]:
            answer[2] += 1

    result = [0, 1, 2]
    result.sort(key=lambda x: (answer[x], -x), reverse=True)
    result = list(filter(lambda x: answer[x] == answer[result[0]], result))
    return list(map(lambda x: x + 1, result))


print(solution([1, 2, 3, 4, 5]))
# 1
