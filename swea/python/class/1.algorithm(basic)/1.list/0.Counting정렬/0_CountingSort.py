# 카운팅 정렬
# arr 원소가 counts 의 인덱스가 되고
# counts 원소가 temps 의 인덱스가 된다

# 1. counts 배열 만들기
# arr 의 최댓값보다 1 큰 배열을 선언한다
# (5를 [5]에 넣으려면 6개 배열이 필요)

max_arr = max(arr) # max() 구현 생략
counts = [0] * (max_arr + 1)
for i in range(N) : # arr  순회
    counts[arr[i]] += 1

print(counts)

# 2. 누적합 구하기
# temps 인덱스와 counts 원소와 같아지려면
# c[0]+c[1]=c[2], c[1]+c[2]=c[3] 가 되어야 한다

for i in range(1, max_arr+1) :
    counts[i] += counts[i-1]

print(counts)

# 3. temps 배열 만들기
# arr 와 크기가 같으므로 N개의 원소를 가지며
# arr 원소를 인덱스로 하는 counts 의 원소를 인덱스로 하는 temps
# temps 에 arr 원소를 넣으면, counts 는 줄여야 한다

temps = [0] * N
for i in range(N) :
    counts[arr[i]] -= 1
    temps[counts[arr[i]]] = arr[i]

print(temps)
