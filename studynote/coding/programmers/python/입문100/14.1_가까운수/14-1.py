def solution(array, n):

    N = len(array)

    diff = []
    for a in array:
        diff += [abs(n-a)]

    ans = [] # 여러개일경우 더 작은 수를 리턴한다
    for idx, item in enumerate(diff):
        if item == min(diff):
            ans += [array[idx]]

    return min(ans)
