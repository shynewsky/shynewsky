def solution(dots):
    dots.sort()
    width = dots[3][0] - dots[0][0]
    height = dots[3][1] - dots[0][1]
    return width * height
