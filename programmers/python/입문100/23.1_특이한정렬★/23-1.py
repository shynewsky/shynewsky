def solution(numlist, n): # [1, 2, 3, 4, 5, 6], 4
    numlist1 = [[abs(n-num),n-num,idx] for idx, num in enumerate(numlist)]
    # 1) 차가 가장 작은 것을 기준으로 정렬 ㅡ abs(n-num)
    # 2) 차가 같다면, n이 더 큰 것을 기준으로 정렬 ㅡ n-num
    # 3) 나중에 인덱스를 활용해서 기존 numlist 에서 answer 로 값복사
    # [[3,3,0],[2,2,1],[1,1,2],[0,0,3],[1,-1,4],[2,-2,5]]
    numlist1.sort()
    # [[0,0,3],[1,-1,4],[1,1,2],[2,-2,5],[2,2,1],[3,3,0]]
    answer = []
    for a, b, c in numlist1:
        answer.append(numlist[c])
    # [4, 5, 3, 6, 2, 1]
    return answer
