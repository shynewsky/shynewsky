import sys
sys.stdin = open('input.txt')

arr = [int(input()) for _ in range(9)] # 9명 난쟁이 키 가져오기
sum_arr = sum(arr)

idx1, idx2 = -1, -1

for i in range(8):
    for j in range(i+1, 9):
        if sum_arr - (arr[i] + arr[j]) == 100 :
            idx1, idx2 = i, j

arr.pop(idx2) # 뒤에서부터 뽑아야 인덱스가 밀리지 않는다
arr.pop(idx1)
arr.sort()
for i in arr :
    print(i)

import sys
sys.stdin = open('input.txt')

arr = [int(input()) for _ in range(9)] # 9명 난쟁이 키 가져오기
sum_arr = sum(arr)

idx1, idx2 = -1, -1

for i in range(8):
    for j in range(i+1, 9):
        if sum_arr - (arr[i] + arr[j]) == 100 :
            idx1, idx2 = i, j

arr.pop(idx2) # 뒤에서부터 뽑아야 인덱스가 밀리지 않는다
arr.pop(idx1)
arr.sort()
for i in arr :
    print(i)

