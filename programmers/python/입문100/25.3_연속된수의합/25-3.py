def solution(k, total):
    answer = []
    # 시작 숫자가 n이고, 개수가 k 일때
    # n*k + ((k-1)*k)/2 = total 이다
    # k와 total을 알면, n = (total - (((k-1)*k)/2))/k
    n = (total - (((k-1)*k)/2))/k
    for i in range(k): # k개 넣기
        answer.append(n+i)
    return answer
