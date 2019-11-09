def solution(s):
    s = s[2:-2].split('},{')
    result = []
    for i in s:
        result.append(list(i.split(',')))
    result.sort(key=lambda x: -len(x))
    answer = []
    while result:
        t = result.pop().pop()
        answer.append(int(t))
        for i in range(len(result)):
            result[i].remove(t)
    return answer


inputs = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",  # [2, 1, 3, 4]
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",  # [2, 1, 3, 4]
    "{{20,111},{111}}",  # [111, 20]
    "{{123}}",  # [123]
    "{{4,2,3},{3},{2,3,4,1},{2,3}}"  # [3, 2, 4, 1]
]

for input123123 in inputs:
    print(solution(input123123))
