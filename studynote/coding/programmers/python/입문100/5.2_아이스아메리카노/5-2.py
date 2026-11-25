def solution(money):
    coffee = money // 5500
    left = money - (coffee * 5500)
    return [coffee, left]
