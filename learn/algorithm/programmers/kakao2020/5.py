print("good")


def solution(n, build_frame):
    arr = [[2] * n for _ in range(n)]

    # [x,y,a,b]
    # [가로,세로,종류,설치삭제] 0 기둥, 1 보 / 0 설치, 1 삭제
    for x, y, a, b in build_frame:
        if b == 0:  # 설치
            if a == 0:  # 기둥
                if y == n - 1 or arr[y - 1][x] == 0 or arr[y][x - 1] == 1:
                    arr[y][x] = 0
            else:  # 보 설치
                if arr[y - 1][x] == 0 or (arr[y][x - 1] == 1 and arr[y][x + 1] == 1) or arr[y - 1][x + 1] == 0:
                    arr[y][x] = 1

        else:  # 삭제
            if a == 0:  # 기둥 삭제
                if arr[y + 1][x] == 0: # 위에 기둥이 있는 경우
                    if arr
            else:  # 보 삭제
                pass

    answer = [[]]
    return answer


inputs = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
          [3, 2, 1, 1]]
print(solution(5, inputs))
print("answer : {}".format([[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]))

# inputs = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
#           [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
# print(solution(5, inputs))
# print("answer : {}".format([[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]))
