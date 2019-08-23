def solution(N, stages):
    usersPass = [0] * (N + 2)
    usersIn = [0] * (N + 2)

    for i in stages:
        usersIn[i] += 1

    usersPass[N+1] = usersIn[N+1]
    for i in range(len(usersPass) - 1, 0, -1):
        usersPass[i - 1] = usersIn[i - 1] + usersPass[i]

    result = []
    for i in range(1, len(usersIn)-1):
        if usersPass[i] == 0:
            result.append((0, i))
        else:
            v = (usersIn[i]/float(usersPass[i]))
            result.append((v, i))

    result.sort(key=myOrder2)
    result.sort(reverse=True, key=myOrder1)

    answer = []
    for i in result:
        answer.append(i[1])
    return answer


def myOrder1(item):
    return item[0]


def myOrder2(item):
    return item[1]
