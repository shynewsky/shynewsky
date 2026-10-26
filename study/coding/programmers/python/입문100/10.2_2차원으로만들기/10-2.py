def solution(num_list, n):
    answer = [[0]*n for _ in range(len(num_list)//n)]
    idx = 0
    for num in num_list:
        answer[idx//n][idx%n] = num
        idx += 1
    return answer
