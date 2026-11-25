# 단순 변수 선언은 한 줄로 줄일 수 있다

max_num, min_num = arr[0], arr[0]

# 같은 역할을 하는 for 문은 하나로 합칠 수 있다

for i in range(0, N):    
    if max_num < arr[i]:
        max_num = arr[i]
    if min_num > arr[i]:
        min_num = arr[i]

#0번은 이미 넣어놨으니, 1번부터 순회해도 된다

for i in range(1, N):   
    if max_v < arr[i]:
        max_v = arr[i]
    if min_v > arr[i]:
        min_v = arr[i]

# 인덱스 대신, 원소 자체로 돌아도 가능하다

for num in nums:         
    if max_num < num:    
        max_num = num    
    elif min_num > num:   
        min_num = num

