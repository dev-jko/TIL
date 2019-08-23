from itertools import combinations

answer = []


def solution(relation):
    n = len(relation[0])
    for i in range(1, n + 1):
        for combi in combinations(range(0, n), i):
            if isSub(set(combi)) or checkSame(combi, relation):
                continue
            t = set(combi)
            answer.append(t)
    return len(answer)


def isSub(a):
    for i in answer:
        if len(i - a) == 0:
            return True
    return False


def checkSame(cols, relation):
    for i in range(0, len(relation)):
        for j in range(i+1, len(relation)):
            if isSame(relation[i], relation[j], cols):
                return True
    return False


def isSame(a, b, cols):
    for i in cols:
        if(a[i] != b[i]):
            return False
    return True
