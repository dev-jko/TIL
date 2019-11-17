def solution(progresses, speeds):
    re = []
    for i in range(len(progresses)):
        t = 100 - progresses[i]
        d = t // speeds[i]
        r = t % speeds[i]
        if r:
            d += 1
        re.append(d)
    answer = [1]
    for i in range(1, len(re)):
        if re[i] <= re[i - 1]:
            answer[-1] += 1
            re[i] = re[i - 1]
        else:
            answer.append(1)
    return answer
