# 방1) try-except

import sys

while True :
    try :
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break

# 방2) ㄱㅁㅈ님

import sys

for num in sys.stdin:
    A, B = map(int, num.split())
    print(A+B)

