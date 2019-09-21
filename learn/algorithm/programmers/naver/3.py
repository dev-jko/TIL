from heapq import heappush, heappop


def solution(data):
    n = len(data)
    for i in range(n):
        data[i][0], data[i][2] = data[i][2], data[i][0]

    answer = []
    time = 0
    data_input_idx = 0
    heap = []

    while data_input_idx < n or heap:
        for i in range(data_input_idx, n):
            if data[i][1] <= time:
                heappush(heap, data[i])
                data_input_idx = i + 1
            else:
                break

        if not heap:
            time = max(time, data[data_input_idx][1])
            heappush(heap, data[data_input_idx])
            data_input_idx += 1

        if heap:
            current = heappop(heap)
            time += current[0]
            answer.append(current[2])

    return answer


main_input = [[1, 2, 10], [2, 5, 8], [3, 6, 9], [4, 20, 6], [5, 25, 5]]
main_answer = [1, 2, 4, 5, 3]
print("output : ")
print(solution(main_input))
print("answer : ")
print(main_answer)
