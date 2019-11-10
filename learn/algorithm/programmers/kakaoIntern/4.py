# def solution(k, room_number):
#     hash = dict()
#     answer = []
#     for room in room_number:
#         while room in hash:
#             t = room
#             room += hash[room]
#             hash[t] += 1
#         hash[room] = 1
#         answer.append(room)
#     return answer


def solution(k, room_number):
    dic = dict()
    answer = []
    for room in room_number:
        if room not in dic:
            dic[room] = Node(room)
            answer.append(room)
        else:
            t = find(dic[room])
            next_room = t.number + 1
            while next_room in dic:
                union(t, dic[next_room])
                t = find(dic[next_room])
                next_room = t.number + 1
            dic[next_room] = Node(next_room)
            union(t, dic[next_room])
            answer.append(next_room)
    return answer


class Node:
    def __init__(self, number):
        self.parent = self
        self.number = number


def find(node):
    if node == node.parent:
        return node
    node.parent = find(node.parent)
    return node.parent


def union(node1, node2):
    parent1 = find(node1)
    parent2 = find(node2)
    if parent1 == parent2:
        return
    if parent1.number < parent2.number:
        parent1.parent = parent2
    else:
        parent2.parent = parent1


# print(solution(10, [1, 3, 4, 1, 3, 1]))
print(solution(10, [1, 3, 4, 1, 3, 1, 1, 1, 1, 1, 1]))
# [1,3,4,2,5,6]
