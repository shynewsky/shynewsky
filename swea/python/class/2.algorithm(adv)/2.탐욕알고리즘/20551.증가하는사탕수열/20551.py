T = int(input())
for t in range(1, T+1):
    A, B, C = map(int, input().split())

    count = 0
    if B >= C : # B가 C보다 크거나 같으면 ㅡ B를 줄인다
        count += B - (C-1)
        B = C-1
    if A >= B : # A가 B보다 크거나 같으면 ㅡ A를 줄인다
        count += A - (B-1)
        A = B-1
    if not (A>0 and B>0 and C>0):
       count = -1
        
    print(f'#{t}', count)
    