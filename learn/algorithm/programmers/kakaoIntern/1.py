def solution(board, moves):
    board = list(map(lambda x: list(reversed(x)), zip(*board)))
    stack = []
    answer = 0
    for move in moves:
        move -= 1
        while board[move] and board[move][-1] == 0:
            board[move].pop()
        if board[move]:
            stack.append(board[move].pop())
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                answer += 2
                stack.pop()
                stack.pop()
    return answer





print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
# 4
