def solution(s):
    answer = len(s)
    for i in range(1, int(len(s) / 2) + 1):
        answer = min(answer, check(i, s))
    return answer


def check(n, string):
    split_string = []
    for i in range(0, len(string), n):
        split_string.append(string[i:i + n])
    result = [[split_string[0], 1]]
    for i in range(1, len(split_string)):
        if split_string[i] == result[-1][0]:
            result[-1][1] += 1
        else:
            result.append([split_string[i], 1])
    return len(''.join(map(lambda x: f'{x[1] if x[1] > 1 else ""}{x[0]}', result)))


print(solution("aabbaccc"))  # 7
