def solution(baseball):
    answers = set()
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i == j or i == k or j == k:
                    continue
                answers.add(str(i * 100 + j * 10 + k))

    for nums, st, ball in baseball:
        nums = str(nums)
        no_answer = set()
        for answer in answers:
            cnt_st = 0
            cnt_ball = 0
            for i in range(3):
                for j in range(3):
                    if nums[i] == answer[j] and i != j:
                        cnt_ball += 1
                    elif nums[i] == answer[j] and i == j:
                        cnt_st += 1
            if cnt_st == st and cnt_ball == ball:
                continue
            else:
                no_answer.add(answer)
        print(answers)
        print(no_answer)
        answers -= no_answer
    return len(answers)


print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
# 2
