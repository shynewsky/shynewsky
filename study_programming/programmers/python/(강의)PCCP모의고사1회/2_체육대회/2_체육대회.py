def solution(ability):

    # 변수 -------------------------------------
    N = len(ability) # 학생 수
    M = len(ability[0]) # 종목 수
    
    visited = [0] * N
    max_total = 0
    
    # 함수 -------------------------------------
    def recur(n, total):
        nonlocal max_total
        
        # 종료조건 - 종목 수
        if n == M:
            # 총합갱신
            max_total = max(max_total, total)
            return
                
        # 경우의수 - 학생수
        for i in range(0, N): 
            # 가지치기 - 중복제거
            if visited[i]:
                continue
                
            visited[i] = 1
            recur(n+1, total+ability[i][n])
            visited[i] = 0

    recur(0, 0)
    return max_total