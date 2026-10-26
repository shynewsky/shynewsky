T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    max_kill = 0

    for row in range(N):
        for column in range(N):
            sum_perpendicular = matrix[row][column]
            sum_diagonal = matrix[row][column]

            for m in range(1, M):
                for x, y in [(-m, 0), (m, 0), (0, -m), (0, m)]:
                    spray_x = row + x
                    spray_y = column + y
                    if 0 <= spray_x < N and 0 <= spray_y < N:
                        sum_perpendicular += matrix[spray_x][spray_y]

                for x, y in [(-m, -m), (-m, m), (m, -m), (m, m)]:
                    spray_x = row + x
                    spray_y = column + y
                    if 0 <= spray_x < N and 0 <= spray_y < N:
                        sum_diagonal += matrix[spray_x][spray_y]

            max_kill = max(max_kill, sum_perpendicular, sum_diagonal)

    print(f"#{test_case} {max_kill}")
