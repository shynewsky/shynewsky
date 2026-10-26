# 1. 이진 최소 힙 -------------------------------------------
def heappush(x):
    heap.append(x)      # 일단 뒤에 붙이고
    i = len(heap) - 1   # 해당 원소의 인덱스를 구한다
    while i > 1:
        p = i // 2      # 해당 원소의 부모 인덱스는, 현재위치의 절반이다
        if heap[i] < heap[p]:
            heap[i], heap[p] = heap[p], heap[i]
            i = p
        else:
            break

# 2. 마지막 노드의 조상 노드에 저장된 정수의 합 -------------------
# 힙의 마지막 노드에서 시작해, 부모를 따라 올라가며 값의 합을 구한다
def func():
    idx = len(heap) - 1    # 마지막 노드
    total = 0
    while idx > 1:
        idx //= 2          # 부모로 이동
        total += heap[idx] # 부모 값 더하기
    return total

# 입력 -----------------------------------------------------
T = int(input())
for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

# 코드 ----------------------------------------------------
    heap = [0] # 1-indexed
    for x in data:
        heappush(x)
    answer = func()

# 출력 ----------------------------------------------------
    print(f'#{t}', answer)
