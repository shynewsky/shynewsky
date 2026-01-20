# 타이머
import time
start = time.time()
# 입출력
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
write = sys.stdout.write
from pprint import pprint
# ---------------------------------



# ---------------------------------
# 입출력
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
pprint(mat)




# 타이머
end = time.time()
print(str(end-start) + '초\n')