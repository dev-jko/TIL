def solution(array, commands):
    answer = []
    for start, end, k in commands:
        answer.append(sorted(array[start - 1:end])[k - 1])
    return answer




# 3 31 34

print(sorted([333, 313131, 343434]))