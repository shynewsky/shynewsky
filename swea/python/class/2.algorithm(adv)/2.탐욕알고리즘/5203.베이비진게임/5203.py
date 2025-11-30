def card_pick():

    # 플레이어 한명이 뽑고
    # 베이비진 확인하고
    # 없으면 다른 한명이 뽑고
    # 베이비진 확인하고
    for i in range(12):
        player[i%2].append(arr[i])
        if babygin(player[i%2]):
            return i%2+1 # 우승자
    else:
        return 0 # 무승부

def babygin(cards):

    n = len(cards)

    if n < 3: # 카드가 3개 미만이면 스킵
        return False

    count = [0]*(10+2) # 0부터 9까지 수 (10개) + 패딩
    for i in range(n): # cards 순회
        count[cards[i]] += 1

    for i in range(10): # count 순회
        if count[i] >= 3 : # triplet 이 있으면
            return True
        elif count[i]>0 and count[i+1]>0 and count[i+2]>0 : # run 있으면
            return True
    else:
        return False

T = int(input())
for t in range(1, T+1):
    # 입력
    arr = list(map(int, input().split()))
    # 변수
    player = [[],[]] # player[0], player[1]
    print(f'#{t}',card_pick())

