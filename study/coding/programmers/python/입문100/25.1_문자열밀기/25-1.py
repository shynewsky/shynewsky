def solution(A, B):
    answer = 0
    A, B = list(A), list(B)
    while A != B :
        B.append(B.pop(0))
        answer += 1
        if answer > len(A):
            answer = -1
            break
    return answer
