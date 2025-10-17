def solution(dots):
    # [0]-[1] 기울기와 [2]-[3] 기울기 비교
    if (dots[0][1]-dots[1][1])/(dots[0][0]-dots[1][0]) == (dots[2][1]-dots[3][1])/(dots[2][0]-dots[3][0]): return 1
    # [0]-[2] 기울기와 [1]-[3] 기울기 비교
    if (dots[0][1]-dots[2][1])/(dots[0][0]-dots[2][0]) == (dots[1][1]-dots[3][1])/(dots[1][0]-dots[3][0]): return 1
    # [0]-[3] 기울기와 [1]-[2] 기울기 비교
    if (dots[0][1]-dots[3][1])/(dots[0][0]-dots[3][0]) == (dots[1][1]-dots[2][1])/(dots[1][0]-dots[2][0]): return 1
    # 3개에도 해당이 되지 않으면 평행 없음
    return 0
