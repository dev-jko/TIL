def is_cross(s1, e1, s2, e2):
    pos = (None, (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2))
    if s1 == s2 or s1 == e2 or e1 == s2 or e1 == e2:
        return True

    xf1, xb1 = min(pos[s1][1], pos[e1][1]), max(pos[s1][1], pos[e1][1])
    yf1, yb1 = min(pos[s1][0], pos[e1][0]), max(pos[s1][0], pos[e1][0])
    xf2, xb2 = min(pos[s2][1], pos[e2][1]), max(pos[s2][1], pos[e2][1])
    yf2, yb2 = min(pos[s2][0], pos[e2][0]), max(pos[s2][0], pos[e2][0])

    if pos[s1][0] == pos[e1][0]:
        if pos[s2][0] == pos[e2][0]:
            return False
        elif pos[s1][0] == 1:
            if xf1 == 0 and xb1 == 2:
                return True
            elif xf1 == 0:
                if xf2 == 0 and yf2 != 1 and yb2 != 1:
                    return True
                elif xf2 == xb2 == 1:
                    return True
            elif xf1 == 1:
                if xf2 == 0 and xb2 == 2:
                    return True
                else:
                    return True
        elif xf1 == 0 and xb1 == 2 and (s2 == (yf1, 1) or e2 == (yf1, 1)):
            return True
    return False


def solution(pattern):
    if len(pattern) < 3:
        return [0]
    # answer = [1] + [2] * (len(pattern) - 3) + [1]
    answer = [0] * (len(pattern))
    # answer = [0] * (len(pattern) - 1)

    for i in range(1, len(pattern)):
        current = [i - 1, i]
        for j in range(1, i):
            line = [j, j + 1]
            if is_cross(*current, *line):
                answer[i - 1] += 1
                # answer[j] += 1

    return answer


inputs = [
    [1, 2, 5, 8, 9],
    [1, 6, 8, 3, 4],
    [2, 5, 1, 3],
    [6, 5, 7, 3, 9],
    [5, 3]
]

outputs = [
    [1, 2, 2, 1],
    [3, 2, 3, 2],
    [2, 2, 2],
    [3, 2, 3, 2],
    [0]
]

for i in range(5):
    print(solution(inputs[i]))
    print(outputs[i])
    print()
