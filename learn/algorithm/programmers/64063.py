import sys
sys.setrecursionlimit(1500)

def find_parent(num, parent):
    if num not in parent:
        parent[num] = num
        return num
    if parent[num] == num:
        return num
    parent[num] = find_parent(parent[num], parent)
    return parent[num]

def solution(k, room_number):
    answer = []
    parent = {}
    for i in room_number:
        temp = find_parent(i, parent)
        answer.append(temp)
        parent[temp] = temp + 1
    return answer