N, M = map(int, input().split())
arr = list(map(int, input().split()))

#--------------------------------------------------

# 부분집합4 (신기욱 강사님)

def recur(arr, n, path, result):
    if n == len(arr):
        result.append(path[:])  # deepcopy
        return

    recur(arr, n + 1, path, result)

    path.append(arr[n])
    recur(arr, n + 1, path, result)
    path.pop()

result = []
recur(arr, 0, [], result)
print(result)

#--------------------------------------------------

# 부분집합5 (김대연님)

def recur(start, curr_sum, count):
    global max_sum

    if curr_sum > M:
        return

    if count == 3:
        if max_sum < curr_sum:
            max_sum = curr_sum
        return

    recur(start+1, curr_sum + arr[start], count+1)
    recur(start+1, curr_sum, count)

    return

max_sum = 0
recur(0, 0, 0)
print(max_sum)

#--------------------------------------------------





# 부분집합6 (한상민님)

def recur(start, count, curr_sum):
    global max_sum

    if curr_sum > M:
        return

    if count == 3:
        if max_sum < curr_sum:
            max_sum = curr_sum
        return

    for i in range(start, N):
        recur(i + 1, count + 1, curr_sum + arr[i])

max_sum = 0
recur(0, 0, 0)
print(max_sum)

#--------------------------------------------------

# 부분집합7 (내 코드ㅠㅠ)

def recur(n, curr_sum):
    global max_sum

    if curr_sum > M:
        return

    if n == 3: # 종료조건 ㅡ 카드를 3개 뽑으면 종료
        if max_sum < curr_sum and curr_sum <= M:
            max_sum = curr_sum
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        recur(n + 1, curr_sum + arr[i])
        visited[i] = 0

visited = [0] * N
max_sum = 0
recur(0, 0)
print(max_sum)

