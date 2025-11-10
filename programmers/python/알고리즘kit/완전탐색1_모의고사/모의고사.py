first = [1, 2, 3, 4, 5]  # 5
second = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10


def solution(answers):
    N = len(answers)
    scores = [0, 0, 0]
    for i in range(N):
        if answers[i] == first[i % 5]:
            scores[0] += 1
        if answers[i] == second[i % 8]:
            scores[1] += 1
        if answers[i] == third[i % 10]:
            scores[2] += 1

    max_score = max(scores)
    result = []
    for i in range(3):
        if max_score == scores[i]:
            result.append(i + 1)
    return result


