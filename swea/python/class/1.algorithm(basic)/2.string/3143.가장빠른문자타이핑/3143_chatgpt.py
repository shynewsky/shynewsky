T = int(input())

for test_case in range(1, T + 1):
    A, B = input().split()
    lenA = len(A)
    lenB = len(B)

    count = 0
    i = 0

    for i in range(lenA):
        # 매칭된 구간을 건너뛰었으면 skip
        if i > 0 and A[i-1:i-1+lenB] == B:
            continue

        # 현재 위치에서 B가 매칭되면 B의 길이만큼 건너뜀
        if A[i:i+lenB] == B:
            count += 1
            # i는 자동으로 +1 되므로, lenB-1만큼 더 건너뜀
            for _ in range(lenB - 1):
                if i < lenA - 1:
                    i += 1
        else:
            count += 1

    print(f"#{test_case} {count}")

