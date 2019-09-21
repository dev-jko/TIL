top_domain = ("com", "net", "org")


def solution(emails):
    answer = 0

    for email in emails:
        t = email.split("@")
        if len(t) != 2 or t[0] == "" or t[1] == "":
            continue
        t = t[1].split(".")
        if len(t) != 2 or t[0] == "" or t[1] == "":
            continue
        if t[1] in top_domain:
            answer += 1
    return answer




main_input = ["f@a.@com.com"]
main_answer = 1
print("output : ")
print(solution(main_input))
print("answer : ")
print(main_answer)
