def solution(my_str, n):
    N = len(my_str)
    answer = [my_str[i:i+n] for i in range(0,N,n)]
    return answer