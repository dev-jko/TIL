def solution(words, queries):
    query_dict = {}
    for i in set(queries):
        query_dict[i] = 0
        for j in words:
            if len(j) != len(i):
                continue
            if i[0] != "?":
                ll = i.find("?")
                if i[:ll] == j[:ll]:
                    query_dict[i] += 1
            else:
                index = len(i) - i[::-1].find("?")
                if i[index:] == j[index:]:
                    query_dict[i] += 1

    answer = []
    for i in queries:
        answer.append(query_dict[i])
    return answer


inputs = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
inputs2 = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(inputs, inputs2))
print("answer : {}".format([3, 2, 4, 1, 0]))
