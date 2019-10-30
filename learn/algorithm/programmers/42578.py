def solution(clothes):
    dic = {}
    for c in clothes:
        if c[1] in dic:
            dic[c[1]] += 1
        else:
            dic[c[1]] = 1
    answer = 1
    for v in dic.values():
        answer *= v + 1
    return answer - 1