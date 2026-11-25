#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())

    base = [2, 3, 5, 7, 11]
    a, b, c, d, e = 0, 0, 0, 0, 0

    isLoop = True
    while isLoop : 
        if N % 2 != 0 : 
            isLoop = False
            break
        N /= 2
        a += 1
        
    isLoop = True
    
    while isLoop : 
        if N % 3 != 0 : 
            isLoop = False
            break
        N /= 3
        b += 1

    isLoop = True
    
    while isLoop : 
        if N % 5 != 0 : 
            isLoop = False
            break
        N /= 5
        c += 1
        
    isLoop = True
    
    while isLoop : 
        if N % 7 != 0 : 
            isLoop = False
            break
        N /= 7
        d += 1

    isLoop = True
    
    while isLoop : 
        if N % 11 != 0 : 
            isLoop = False
            break
        N /= 11
        e += 1

    print(f'#{test_case} {a} {b} {c} {d} {e}')