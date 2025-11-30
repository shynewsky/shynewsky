from collections import deque

T = int(input()) # 테스트 케이수 수

for test_case in range(1, T+1):

    # 입력
    N, M = map(int, input().split()) # N 화덕크기, M 피자개수
    arr = list(map(int, input().split())) # 피자 M개, 치즈 양

    # 피자 리스트 만들기
    # deque([[1, 7], [2, 2], [3, 6], [4, 5], [5, 3]])
    pizza_list = deque()
    for idx, item in enumerate(arr):
        pizza_list.append([idx+1, item])

    # 화덕 만들기
    # deque([[1, 7], [2, 2], [3, 6]])
    cook_list = deque()
    for i in range(N): # 화덕 칸 만큼
        cook_list.append(pizza_list.popleft())

    # 요리하기
    num = 0
    while len(cook_list) > 1 :

        # 가장 앞에 있는 것을 빼서 치즈를 녹이고, 치즈 상태를 확인한다
        pizza = cook_list.popleft()
        pizza[1] //= 2

        if pizza[1] != 0: # 치즈가 0이 아니면
            cook_list.append(pizza)
        else :
            if pizza_list:
                cook_list.append(pizza_list.popleft())

    print(f'#{test_case}', cook_list[0][0])
