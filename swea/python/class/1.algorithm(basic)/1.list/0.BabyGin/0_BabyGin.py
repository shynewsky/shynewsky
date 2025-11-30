# 카운팅 정렬의 개념을 사용한다
# 1. 0~9까지의 숫자만 존재하므로, 0~9 인덱스가 존재하는 10개짜리 counts 배열을 만든다
# 2. counts 배열에 각 카드가 몇개씩 있는지 채워넣는다
# 3. 같은 숫자가 3개 이상이면 triplet, 연속된 숫자가 3개있으면 run
# 4. triplet 2쌍, run 2쌍, triplet/run 1쌍씩 ㅡ babygin

counts = [0] * 10
babygin = 0

for i in range(N) : # arr 순회
    counts[arr[i]] += 1 # counts 배열 채우기

for i in range(10 - 1) :

    while True : # 같은 숫자가 6장 있거나(333333), 연속된 숫자가 2장씩 있거나(123123)

        # triplet 검색
        if counts[i] >= 3 : # 같은 숫자가 3장일때
            counts[i] -= 3
            babygin += 1

        # run 검색 ㅡ 연속3개가 1일때
        elif counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1 :
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            babygin += 1

        else : # 더이상 없으면 탈출
            break

print(f'#{test_case} {babygin // 2}')

