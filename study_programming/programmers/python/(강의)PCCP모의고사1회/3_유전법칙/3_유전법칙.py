# ChatGPT

'''
"n 세대의 p번쨰 애의 gene 은 뭐야?"

<올라갈떄 : 내 부모 누구지?>
- 바로 위 n-1 세대의 부모를 보면 된다
    - 3세대 1~4번 → 2세대 1번
    - 3세대 5~8번 → 2세대 2번
    ...
- 그 부모는 누구의 자식인가?
    - 2세대 1~4번 → 1세대 1번
    ...

<내려올떄 : 나는 몇번쨰 자식이지?>
- 이제 다시 내려오면서 판단
    - 부모가 RR이면 → 자식 전부 RR
    - 부모가 rr이면 → 자식 전부 rr
    - 부모가 Rr이면 → 자식 RR Rr Rr rr
'''

def solution(queries):
    
    # 함수 ---------------------------------------------
    def recur(n, p):

        # 1세대는 Rr 자가교배
        if n == 1:
            return "Rr"
        
        # 1.내 부모 누구지?
        parent_p = (p - 1) // 4 + 1          # 부모는 n-1세대의 몇번쨰
        parent_gene = recur(n - 1, parent_p) # 이전세대로 올라가면서 부모 유전자 받아옴        

        if parent_gene == "RR":
            return "RR"
        elif parent_gene == "rr":
            return "rr"
        elif parent_gene == 'Rr':
                    
            # 2. 부모가 Rr 일 경우 → 나는 몇번째 자식이지?
            child_order = (p - 1) % 4

            if child_order == 0:
                return "RR"
            elif child_order == 3:
                return "rr"
            elif child_order == 1 or child_order == 2:
                return "Rr"
    
    # 코드 ---------------------------------------------
    answer = []
    
    for n, p in queries:
        answer.append(recur(n, p))
    
    return answer