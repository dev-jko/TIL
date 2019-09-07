def split_str(s, n):
    result = []
    i = 0
    leng = len(s)
    while i < leng:
        if i + n > leng:
            result.append(s[i:])
            break
        result.append(s[i:i + n])
        i += n

    return result


def count_str(ss):
    i = 0
    result = ""
    while i < len(ss):
        cnt = 0
        while i + cnt < len(ss) and ss[i] == ss[i + cnt]:
            cnt += 1
        if cnt == 1:
            result += ss[i]
        else:
            result += "{}{}".format(cnt, ss[i])
        i += cnt
    return len(result)


def solution(s):
    answer = len(s)
    for i in range(1, len(s) + 1):
        ss = split_str(s, i)
        t = count_str(ss)
        if answer > t:
            answer = t
    return answer



inputs = "aabbaccc"  # 7
# print(split_str(inputs, 3), sep="=")
print(solution(inputs))
