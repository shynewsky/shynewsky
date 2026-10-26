def solution(n):
    answer = []
    num = 1
    while len(answer) < n:
        if num % 3 != 0 and '3' not in str(num):
            answer.append(num)
        num += 1

    return answer[-1]
