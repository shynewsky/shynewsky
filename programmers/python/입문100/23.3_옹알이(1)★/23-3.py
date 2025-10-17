def solution(babbling):
    cnt = 0  # 발음할 수 있는 단어
    for word in babbling:
        i = 0  # 인덱스 초기화
        N = len(word)  # 단어의 길이
        while i < N:  # 단어가 끝날때까지
            if word[i:i + 3] == 'aya':
                print(word, word[i:i + 3])
                i += 3
            elif word[i:i + 2] == 'ye':
                print(word, word[i:i + 2])
                i += 2
            elif word[i:i + 3] == 'woo':
                print(word, word[i:i + 3])
                i += 3
            elif word[i:i + 2] == 'ma':
                print(word, word[i:i + 2])
                i += 2
            else: # 가지치기
                break
            # 단어가 완성됐으면 하나 증가
            if i == N:
                cnt += 1

    return cnt
