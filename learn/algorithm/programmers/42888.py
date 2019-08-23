def solution(record):
    result = []
    nick = {}
    msg = ("님이 들어왔습니다.", "님이 나갔습니다.")

    for s in record:
        s = s.split()
        if s[0] == "Enter":
            nick[s[1]] = s[2]
            result.append((s[1], 0))
        elif s[0] == "Change":
            nick[s[1]] = s[2]
        else:
            result.append((s[1], 1))

    answer = []
    for i in result:
        temp = nick[i[0]] + msg[i[1]]
        answer.append(temp)

    return answer
