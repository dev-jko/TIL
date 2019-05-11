def solution(s):
    count = [0] * 5
    for i in range(len(s)):
        count[s[i]] += 1
    one_three = min(count[1], count[3])
    count[1] -= one_three
    count[3] -= one_three
    two_two = count[2] // 2
    count[2] = count[2] % 2
    answer = count[4] + one_three + two_two
    if count[3] != 0:
        answer += count[3] + count[2]
    else:
        answer += count[2]
        count[1] -= count[2] * 2
        if count[1] > 0:
            one = count[1] // 4
            count[1] = count[1] % 4
            answer += one + (1 if count[1] > 0 else 0)
    return answer
