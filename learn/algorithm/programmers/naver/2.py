move = {"#": (0, 1), "*": (0, 1), ">": (1, 0), "<": (-1, 0)}


def simul(start, drum):
    x, y, n, used = start, 0, len(drum), False
    while (y < n):
        next = drum[y][x]
        if next == "*":
            if used:
                return False
            else:
                used = True
        t = move[next]
        x += t[0]
        y += t[1]
    return True


def solution(drum):
    answer = 0
    for i in range(len(drum)):
        if simul(i, drum):
            answer += 1
    return answer


main_input = ["######", ">#*###", "####*#", "#<#>>#", ">#*#*<", "######"]
main_answer = 4
print("output : ")
print(solution(main_input))
print("answer : ")
print(main_answer)
