def solution(N, stages):

    arr = []
    
    for i in range(1, N+1): # 스테이지 번호
        a = stages.count(i) # 통과못한 사람(i)
        b = 0               # 시도한 사람(i이상)
        
        for j in stages:    # 플레이어 위치
            if i <= j:
                b += 1
                
        if b == 0:
            arr.append([0, i])
            continue
            
        arr.append([a/b, i]) # 실패율, 스테이지번호
        
    arr.sort(key=lambda x : (-x[0], x[1]))
    return [b for a, b in arr]
