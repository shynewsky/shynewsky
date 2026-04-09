import time
start = time.time()
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
# -------------------------------

# 함수
def alphabet(c):
    print(ord(c))
    print(ord('A'))
    print(ord(c) - ord('A'))
    return ord(c) - ord('A')

def solution(N, S):
    answer = 0
    for i in range(N):
        print(i)
        print(alphabet(S[i]))
        answer += alphabet(S[i]) * (31 ** i)
        print()

    print(answer)


# 코드
length = int(input())
string = input().strip()
solution(length, string)

# -------------------------------
end = time.time()
print(end-start, '초')