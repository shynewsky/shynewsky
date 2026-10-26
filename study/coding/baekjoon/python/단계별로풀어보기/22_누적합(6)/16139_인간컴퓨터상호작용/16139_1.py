# 타이머
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
from pprint import pprint
# ----------------------------------------

S = input().strip() # 문자열
'실수1 : 문자열 끝에 뭐가 붙어 있는지 생각해봐'

# 누적합
# - 알파벳은 26개로 고정 -> 미리 누적합
# - 배열 26개 변수명 많음 -> 행렬

l = len(S) # 문자열S 길이
arr = 'abcdefghijklmnopqrstuvwxyz'
mat = [[0] * l for _ in range(26)]

for i in range(26): # abc 길이
    for j in range(l): # 문자열S 길이
        '실수2 : j가 0일 때 j-1 은?'
        if j == 0:
            if arr[i] != S[j]:
                mat[i][j] = 0
            elif arr[i] == S[j]:
                mat[i][j] = 1
        else :
            if arr[i] != S[j]:
                mat[i][j] = mat[i][j-1]
            elif arr[i] == S[j]:
                mat[i][j] = mat[i][j-1] + 1

# 질문 : [l, r+1] 구간에서의 a의 개수
q = int(input()) # 질문의수
out = [0]
for _ in range(q):
    a, l, r = input().split()
    '실수3 : “r번째 문자를 포함해서 생각한다”의 정확한 의미 = [r까지 누적] − [(l−1)까지 누적]'
    if int(l) == 0:
        '실수4 : 문자는 정수 인덱스로 바로 변환 가능 : arr.index(a) -> ord(a) - 97'
        write(str(mat[ord(a) - 97][int(r)]))
    else :
        write(str(mat[ord(a) - 97][int(r)] - mat[ord(a) - 97][int(l)-1]))
    write('\n')

# ----------------------------------------
# 타이머
end = time.time()
write(str(end-start) + '초')