def solution(k, room_number):
    hash = dict()
    answer = []
    for room in room_number:
        while room in hash:
            t = room
            room += hash[room]
            hash[t] += 1
        hash[room] = 1
        answer.append(room)
    return answer


# print(solution(10, [1, 3, 4, 1, 3, 1]))
print(solution(10, [1, 3, 4, 1, 3, 1, 1, 1, 1, 1, 1]))
# [1,3,4,2,5,6]
